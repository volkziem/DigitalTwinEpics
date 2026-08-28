# show_bpm.py, V. Ziemann, 260819
import epics
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

def on_close(event):
  plt.ioff()
  sys.exit()
    
plt.ion()

fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)

bpmx=['DT:IPM2I00:XPOS','DT:IPM2I00A:XPOS','DT:IPM2I01A:XPOS',
      'DT:IPM1I02:XPOS', 'DT:IPM1I03:XPOS', 'DT:IPM1I04:XPOS',
      'DT:IPM1I05:XPOS', 'DT:IPM1I07:XPOS', 'DT:IPM0I01:XPOS',
      'DT:IPM0I01B:XPOS']

bpmy=['DT:IPM2I00:YPOS','DT:IPM2I00A:YPOS','DT:IPM2I01A:YPOS',
      'DT:IPM1I02:YPOS', 'DT:IPM1I03:YPOS', 'DT:IPM1I04:YPOS',
      'DT:IPM1I05:YPOS', 'DT:IPM1I07:YPOS', 'DT:IPM0I01:YPOS',
      'DT:IPM0I01B:YPOS']

while True:
  bpmxpos=epics.caget_many(bpmx)
  bpmypos=epics.caget_many(bpmy)
  xrms=np.std(bpmxpos)
  yrms=np.std(bpmypos)
  plt.clf()
  plt.subplot(2,1,1)
  plt.bar(range(len(bpmxpos)),bpmxpos,color='blue')
  plt.ylabel('x [mm]')
  plt.ylim([-5,5])
  plt.text(0,3,"rms = {:.2f}".format(xrms))
  plt.title(' Horizontal and Vertical BPM')
  plt.subplot(2,1,2)
  plt.bar(range(len(bpmypos)),bpmypos,color='red')
  plt.ylabel('y [mm]')
  plt.ylim([-5,5])
  plt.text(0,3,"rms = {:.2f}".format(yrms))
  plt.draw()
  plt.pause(1) 
  
plt.ioff()
plt.show()
  
