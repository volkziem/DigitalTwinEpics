% find_bpm.m, V. Ziemann, 250508
function [bpmpos,corpos,quadpos,solpos,loc2seg,seg2loc]=find_bpm(beamline)
nlines=size(beamline,1);
ib=0;
ic=0;
iq=0;
is=0;
iseg=1;
for line=1:nlines
  for seg=1:beamline(line,2)
    iseg=iseg+1;
    loc2seg(line)=iseg;
    seg2loc(iseg)=line;
    switch beamline(line,1)
      case 103  % BPM
        ib=ib+1;
        bpmpos(ib)=iseg;
      case 7    % corrector
        ic=ic+1;
        corpos(ic)=line;
      case 5    % quadrupole
        iq=iq+1;
        quadpos(iq)=line;
      case 19   % solenoid
        is=is+1;
        solpos(is)=line;  
    end
  end  % for seg
end % for line