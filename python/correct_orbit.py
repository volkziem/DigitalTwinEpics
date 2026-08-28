# correct_orbit.py, V. Ziemann, 260806
import epics,sys,time
import numpy as np

np.set_printoptions(precision=3, suppress=True)
   
c=[]
with open("../matlab/corlist.txt", "r") as file:
    for line in file:
        c.append(line.strip())
corlist=[]
for cor in c:
    corlist.append('DT:'+cor+'H:BDL')
for cor in c:
    corlist.append('DT:'+cor+'V:BDL')
print('correctors=',corlist)

b=[]
with open("../matlab/bpmlist.txt", "r") as file:
    for line in file:
        b.append(line.strip())
bpms=[]
for bpm in b:
    bpms.append('DT:'+bpm+':XPOS')
for bpm in b:
    bpms.append('DT:'+bpm+':YPOS')
print('BPM=',bpms)

ORM=np.load('response_matrix.npy')
#print('ORM=',ORM)
CM=np.linalg.pinv(ORM,1e-4)
#print("cond=",np.linalg.cond(CM))

# read the BPMs and the correctors
x=np.array(epics.caget_many(bpms))
corval0=np.array(epics.caget_many(corlist))
print('corval0=',corval0)

# calculate the required correction and add to provious
dcorval=-CM @ x
print('dcorval =',dcorval)
corval=corval0+dcorval
print('corval =',corval)
epics.caput('DT:INHIBIT',1)  # only for Twin
epics.caput_many(corlist,corval)
time.sleep(5)
epics.caput('DT:INHIBIT',0)  # only for Twin
print("Done")
