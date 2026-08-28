import tkinter as tk
import epics

root = tk.Tk()
root.title("Magnets")
root.geometry("700x250")

def show_value_MFX2I01_US(val):
  # print(f"Current Value: {val} and name=MFX2I01_US")
  epics.caput('DT:MFX2I01_US:BDL',val)

f_MFX2I01_US=tk.Frame(root)
f_MFX2I01_US.pack(side="left")
c=tk.Canvas(f_MFX2I01_US, width=50, height=130)
c.create_text(40, 60, text="MFX2I01_US", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFX2I01_US, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFX2I01_US)
slider.pack(side="top")

vv=epics.caget('DT:MFX2I01_US:BDL')
slider.set(vv)

def show_value_MFX2I01_DS(val):
  # print(f"Current Value: {val} and name=MFX2I01_DS")
  epics.caput('DT:MFX2I01_DS:BDL',val)

f_MFX2I01_DS=tk.Frame(root)
f_MFX2I01_DS.pack(side="left")
c=tk.Canvas(f_MFX2I01_DS, width=50, height=130)
c.create_text(40, 60, text="MFX2I01_DS", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFX2I01_DS, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFX2I01_DS)
slider.pack(side="top")

vv=epics.caget('DT:MFX2I01_DS:BDL')
slider.set(vv)

def show_value_MFX1I03_US(val):
  # print(f"Current Value: {val} and name=MFX1I03_US")
  epics.caput('DT:MFX1I03_US:BDL',val)

f_MFX1I03_US=tk.Frame(root)
f_MFX1I03_US.pack(side="left")
c=tk.Canvas(f_MFX1I03_US, width=50, height=130)
c.create_text(40, 60, text="MFX1I03_US", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFX1I03_US, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFX1I03_US)
slider.pack(side="top")

vv=epics.caget('DT:MFX1I03_US:BDL')
slider.set(vv)

def show_value_MFX1I03_DS(val):
  # print(f"Current Value: {val} and name=MFX1I03_DS")
  epics.caput('DT:MFX1I03_DS:BDL',val)

f_MFX1I03_DS=tk.Frame(root)
f_MFX1I03_DS.pack(side="left")
c=tk.Canvas(f_MFX1I03_DS, width=50, height=130)
c.create_text(40, 60, text="MFX1I03_DS", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFX1I03_DS, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFX1I03_DS)
slider.pack(side="top")

vv=epics.caget('DT:MFX1I03_DS:BDL')
slider.set(vv)

def show_value_MQW1I03(val):
  # print(f"Current Value: {val} and name=MQW1I03")
  epics.caput('DT:MQW1I03:BDL',val)

f_MQW1I03=tk.Frame(root)
f_MQW1I03.pack(side="left")
c=tk.Canvas(f_MQW1I03, width=50, height=130)
c.create_text(40, 60, text="MQW1I03", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQW1I03, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MQW1I03)
slider.pack(side="top")

vv=epics.caget('DT:MQW1I03:BDL')
slider.set(vv)

def show_value_MQW1I04(val):
  # print(f"Current Value: {val} and name=MQW1I04")
  epics.caput('DT:MQW1I04:BDL',val)

f_MQW1I04=tk.Frame(root)
f_MQW1I04.pack(side="left")
c=tk.Canvas(f_MQW1I04, width=50, height=130)
c.create_text(40, 60, text="MQW1I04", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQW1I04, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MQW1I04)
slider.pack(side="top")

vv=epics.caget('DT:MQW1I04:BDL')
slider.set(vv)

def show_value_MFG1I04A(val):
  # print(f"Current Value: {val} and name=MFG1I04A")
  epics.caput('DT:MFG1I04A:BDL',val)

f_MFG1I04A=tk.Frame(root)
f_MFG1I04A.pack(side="left")
c=tk.Canvas(f_MFG1I04A, width=50, height=130)
c.create_text(40, 60, text="MFG1I04A", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFG1I04A, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFG1I04A)
slider.pack(side="top")

vv=epics.caget('DT:MFG1I04A:BDL')
slider.set(vv)

def show_value_MFG1I04B(val):
  # print(f"Current Value: {val} and name=MFG1I04B")
  epics.caput('DT:MFG1I04B:BDL',val)

f_MFG1I04B=tk.Frame(root)
f_MFG1I04B.pack(side="left")
c=tk.Canvas(f_MFG1I04B, width=50, height=130)
c.create_text(40, 60, text="MFG1I04B", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFG1I04B, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFG1I04B)
slider.pack(side="top")

vv=epics.caget('DT:MFG1I04B:BDL')
slider.set(vv)

def show_value_MQW1I05(val):
  # print(f"Current Value: {val} and name=MQW1I05")
  epics.caput('DT:MQW1I05:BDL',val)

f_MQW1I05=tk.Frame(root)
f_MQW1I05.pack(side="left")
c=tk.Canvas(f_MQW1I05, width=50, height=130)
c.create_text(40, 60, text="MQW1I05", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQW1I05, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MQW1I05)
slider.pack(side="top")

vv=epics.caget('DT:MQW1I05:BDL')
slider.set(vv)

def show_value_MQW1I06(val):
  # print(f"Current Value: {val} and name=MQW1I06")
  epics.caput('DT:MQW1I06:BDL',val)

f_MQW1I06=tk.Frame(root)
f_MQW1I06.pack(side="left")
c=tk.Canvas(f_MQW1I06, width=50, height=130)
c.create_text(40, 60, text="MQW1I06", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQW1I06, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MQW1I06)
slider.pack(side="top")

vv=epics.caget('DT:MQW1I06:BDL')
slider.set(vv)

def show_value_MFX0I01_US(val):
  # print(f"Current Value: {val} and name=MFX0I01_US")
  epics.caput('DT:MFX0I01_US:BDL',val)

f_MFX0I01_US=tk.Frame(root)
f_MFX0I01_US.pack(side="left")
c=tk.Canvas(f_MFX0I01_US, width=50, height=130)
c.create_text(40, 60, text="MFX0I01_US", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFX0I01_US, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFX0I01_US)
slider.pack(side="top")

vv=epics.caget('DT:MFX0I01_US:BDL')
slider.set(vv)

def show_value_MFX0I01_DS(val):
  # print(f"Current Value: {val} and name=MFX0I01_DS")
  epics.caput('DT:MFX0I01_DS:BDL',val)

f_MFX0I01_DS=tk.Frame(root)
f_MFX0I01_DS.pack(side="left")
c=tk.Canvas(f_MFX0I01_DS, width=50, height=130)
c.create_text(40, 60, text="MFX0I01_DS", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFX0I01_DS, from_=50, to=-50, resolution=0.5,
   orient="vertical", command=show_value_MFX0I01_DS)
slider.pack(side="top")

vv=epics.caget('DT:MFX0I01_DS:BDL')
slider.set(vv)

root.mainloop()