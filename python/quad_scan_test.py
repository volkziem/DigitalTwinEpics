# quad_scan_test.py, V. Ziemann, 260821
import epics, time
import numpy as np
import matplotlib.pyplot as plt

PS='DT:MFX2I01:BDL'


v0=-10.49
scanrange=np.arange(v0,v0+7.5,1)
sigx=[]
sigy=[]

for v in scanrange:
  epics.caput(PS,v)
  time.sleep(3)
  epics.caput('DT:SCREEN','ITV1I03')
  time.sleep(2)
  sigmas=epics.caget('DT:SIGMAS')
  print(v,sigmas[0],sigmas[1],sigmas[2])
  sigx.append(sigmas[0])
  sigy.append(sigmas[1])
  
epics.caput(PS,v0)

plt.plot(scanrange,sigx,'-*',label='sigmax')
plt.plot(scanrange,sigy,'-*',label='sigmay')
plt.ylabel('sigmax, sigmay [mm]')
plt.xlabel(PS)
plt.legend()
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
plt.show()
