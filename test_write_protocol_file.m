%test_write_protocol_file.m
clear all

fpd=fopen('test.db','w');
fpp=fopen('test.proto','w');

add_magnet_to_protocol_file(fpd,fpp,'MQW1I04');
add_magnet_to_protocol_file(fpd,fpp,'MQW1I05');

fclose(fpd);
fclose(fpp);

