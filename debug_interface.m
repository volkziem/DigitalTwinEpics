% debug_interface.m, V. Ziemann, 260807
try 
    if strfind(line,'@?')==1      % get parameter
      ii=sscanf(line,"@? %f %f");
      reply=sprintf('@ %d %d %f',ii(1),ii(2),beamline(ii(1),ii(2)));
      writeline(s,reply);
    elseif strfind(line,'@ ')==1  % set parameter
      ii=sscanf(line,"@  %f %f %f");
      beamline(ii(1),ii(2))=ii(3); 
    end
catch 
    writeline(s,'*** Input error')
end  % of try