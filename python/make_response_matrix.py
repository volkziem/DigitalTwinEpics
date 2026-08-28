# make_response_matrix.py, V. Ziemann, 260824
import epics, time, sys
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
print(corlist)

b=[]
with open("../matlab/bpmlist.txt", "r") as file:
    for line in file:
        b.append(line.strip())
bpms=[]
for bpm in b:
    bpms.append('DT:'+bpm+':XPOS')
for bpm in b:
    bpms.append('DT:'+bpm+':YPOS')
print(bpms)
 
ncor=len(corlist)
nbpm=len(bpms)
print(ncor,nbpm)
ORM=np.zeros((ncor,nbpm))

ic=-1
for cornam in corlist:
    print(cornam)
    ic=ic+1
    val0=epics.caget(cornam)
    time.sleep(2)
    x0=np.array(epics.caget_many(bpms))
    val1=val0+1
    print(cornam,val0,'->',val1)
    epics.caput(cornam,val1)
    time.sleep(5)
    x1=np.array(epics.caget_many(bpms))
    ORM[ic,:]=[*(x1-x0)]
    epics.caput(cornam,val0)
    time.sleep(5)

ORM=ORM.T
print(ORM)
np.save('response_matrix.npy',ORM)
np.savetxt('response_matrix.csv',ORM)

#print(x1)
#print(x1-x0)