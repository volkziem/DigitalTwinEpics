% calcmat.m, calculate the transfer-matrices
function [Racc,spos,nmat,nlines,state]=calcmat(beamline,state0)
if nargin<2, state0=zeros(4,1); end
ndim=size(DD(1),1);  
nlines=size(beamline,1);      % number of lines in beamline
nmat=sum(beamline(:,2))+1;    % sum over repeat-count in column 2
Racc=zeros(ndim,ndim,nmat);   % matrices from start to element-end
Racc(:,:,1)=eye(ndim);        % initialize first with unit matrix
state=zeros(4,ndim);          % tracectory
state(:,1)=state0;            % initialize
spos=zeros(nmat,1);           % longitudinal position
ic=1;                         % element counter
for line=1:nlines             % loop over input elements
  for seg=1:beamline(line,2)  % loop over repeat-count 
     ic=ic+1;                 % next element          
     Rcurr=eye(4);            % matrix in next element
     dstate=zeros(4,1);
     switch beamline(line,1) 
       case 0   % marker
         % do nothing
       case {1, 110}   % drift or screen
         Rcurr=DD(beamline(line,3));
         % if (abs(beamline(line,4))>0) 
         %   Rcurr=SOL(beamline(line,3),beamline(line,4));
         % end
       case 2   % thin quadrupole
         Rcurr=Q(beamline(line,4)); 
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 4   % sector dipole
         phi=beamline(line,4)*pi/180;  % convert to radians
         rho=beamline(line,3)/phi;
         Rcurr=SB(beamline(line,3),rho);  
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 5   % thick quadrupole
         Rcurr=QQ(beamline(line,3),beamline(line,4));
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 7   % corrector
         Rcurr=eye(4);
         dstate=[0; beamline(line,5); 0; beamline(line,6)];  % kick
       case 19  % solenoid
         Rcurr=SOL(beamline(line,3),beamline(line,4)); 
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 20  % coordinate roll
         Rcurr=ROLL(beamline(line,4));
       case 21  % thin skew quadrupole
         Rcurr=SQ(beamline(line,4));
       case 22  % thin quad with 1/F as argument
         Rcurr(2,1)=-beamline(line,4);
         Rcurr(4,3)=beamline(line,4);
       case 23  % thin skew quad with 1/F as argument 
         Rcurr(2,3)=beamline(line,4);
         Rcurr(4,1)=beamline(line,4);
       case 24  % thin solenoid with ksL as argument
         Rcurr=SOL(1.0,beamline(line,4)); 
       case 25  % extra drift space
         Rcurr=DD(beamline(line,4));  % length in beamline(*,4)
       case 30  % Vertical Wien Filter, psi=beamline(:,4)
         psi=beamline(line,4)/beamline(line,2);
         Rcurr=VWIEN(beamline(line,3),psi);
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 31  % Horizontal Wien Filter
         psi=beamline(line,4)/beamline(line,2);
         Rcurr=HWIEN(beamline(line,3),psi);
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 44  % rectangular dipole
         phi=beamline(line,4)*pi/180;  % convert to radians
         rho=beamline(line,3)/phi;
         Rcurr=RB(beamline(line,3),rho);
         dstate=(Rcurr-eye(ndim))*[beamline(line,5); 0; beamline(line,6);0];
       case 103 % BPM
         Rcurr=eye(4);
       case 200  % GunHV
         Rcurr=eye(4);
         gamma0=(511+beamline(line,4))/511;
       case 300  % special matrix
         fn=strcat("TM",num2str(300+beamline(line,4)),".dat");
         Rcurr=csvread(fn);
         %Rcurr=csvread("DUT.dat");
       otherwise
         %current_line=line;
         disp('unsupported code')
     end		  
     Racc(:,:,ic)=Rcurr*Racc(:,:,ic-1);    % concatenate 
     spos(ic)=spos(ic-1)+beamline(line,3); % position of element  
     state(:,ic)=Rcurr*state(:,ic-1)+dstate;
  end
end