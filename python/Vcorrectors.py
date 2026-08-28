import tkinter as tk
import epics

root = tk.Tk()
root.title("Injector correctors V")
root.geometry("700x250")

def show_value_MBH2I00V(val):
  # print(f"Current Value: {val} and name=MBH2I00V:BDL")
  epics.caput('DT:MBH2I00V:BDL',val)

f_MBH2I00V=tk.Frame(root)
f_MBH2I00V.pack(side="left")
c=tk.Canvas(f_MBH2I00V, width=50, height=130)
c.create_text(40, 60, text="MBH2I00V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I00V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I00V)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I00V:BDL')
slider.set(vv)

def show_value_MBH2I00AV(val):
  # print(f"Current Value: {val} and name=MBH2I00AV:BDL")
  epics.caput('DT:MBH2I00AV:BDL',val)

f_MBH2I00AV=tk.Frame(root)
f_MBH2I00AV.pack(side="left")
c=tk.Canvas(f_MBH2I00AV, width=50, height=130)
c.create_text(40, 60, text="MBH2I00AV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I00AV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I00AV)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I00AV:BDL')
slider.set(vv)

def show_value_MBH2I01V(val):
  # print(f"Current Value: {val} and name=MBH2I01V:BDL")
  epics.caput('DT:MBH2I01V:BDL',val)

f_MBH2I01V=tk.Frame(root)
f_MBH2I01V.pack(side="left")
c=tk.Canvas(f_MBH2I01V, width=50, height=130)
c.create_text(40, 60, text="MBH2I01V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I01V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I01V)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I01V:BDL')
slider.set(vv)

def show_value_MBH2I01AV(val):
  # print(f"Current Value: {val} and name=MBH2I01AV:BDL")
  epics.caput('DT:MBH2I01AV:BDL',val)

f_MBH2I01AV=tk.Frame(root)
f_MBH2I01AV.pack(side="left")
c=tk.Canvas(f_MBH2I01AV, width=50, height=130)
c.create_text(40, 60, text="MBH2I01AV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I01AV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I01AV)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I01AV:BDL')
slider.set(vv)

def show_value_MBH1I02V(val):
  # print(f"Current Value: {val} and name=MBH1I02V:BDL")
  epics.caput('DT:MBH1I02V:BDL',val)

f_MBH1I02V=tk.Frame(root)
f_MBH1I02V.pack(side="left")
c=tk.Canvas(f_MBH1I02V, width=50, height=130)
c.create_text(40, 60, text="MBH1I02V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I02V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I02V)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I02V:BDL')
slider.set(vv)

def show_value_MBH1I03V(val):
  # print(f"Current Value: {val} and name=MBH1I03V:BDL")
  epics.caput('DT:MBH1I03V:BDL',val)

f_MBH1I03V=tk.Frame(root)
f_MBH1I03V.pack(side="left")
c=tk.Canvas(f_MBH1I03V, width=50, height=130)
c.create_text(40, 60, text="MBH1I03V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I03V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I03V)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I03V:BDL')
slider.set(vv)

def show_value_MBH1I04V(val):
  # print(f"Current Value: {val} and name=MBH1I04V:BDL")
  epics.caput('DT:MBH1I04V:BDL',val)

f_MBH1I04V=tk.Frame(root)
f_MBH1I04V.pack(side="left")
c=tk.Canvas(f_MBH1I04V, width=50, height=130)
c.create_text(40, 60, text="MBH1I04V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I04V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I04V)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I04V:BDL')
slider.set(vv)

def show_value_MBH1I05V(val):
  # print(f"Current Value: {val} and name=MBH1I05V:BDL")
  epics.caput('DT:MBH1I05V:BDL',val)

f_MBH1I05V=tk.Frame(root)
f_MBH1I05V.pack(side="left")
c=tk.Canvas(f_MBH1I05V, width=50, height=130)
c.create_text(40, 60, text="MBH1I05V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I05V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I05V)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I05V:BDL')
slider.set(vv)

def show_value_MBH1I07V(val):
  # print(f"Current Value: {val} and name=MBH1I07V:BDL")
  epics.caput('DT:MBH1I07V:BDL',val)

f_MBH1I07V=tk.Frame(root)
f_MBH1I07V.pack(side="left")
c=tk.Canvas(f_MBH1I07V, width=50, height=130)
c.create_text(40, 60, text="MBH1I07V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I07V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I07V)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I07V:BDL')
slider.set(vv)

def show_value_MBH0I01V(val):
  # print(f"Current Value: {val} and name=MBH0I01V:BDL")
  epics.caput('DT:MBH0I01V:BDL',val)

f_MBH0I01V=tk.Frame(root)
f_MBH0I01V.pack(side="left")
c=tk.Canvas(f_MBH0I01V, width=50, height=130)
c.create_text(40, 60, text="MBH0I01V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH0I01V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH0I01V)
slider.pack(side="top")

vv=epics.caget('DT:MBH0I01V:BDL')
slider.set(vv)

def show_value_MHD0I01AV(val):
  # print(f"Current Value: {val} and name=MHD0I01AV:BDL")
  epics.caput('DT:MHD0I01AV:BDL',val)

f_MHD0I01AV=tk.Frame(root)
f_MHD0I01AV.pack(side="left")
c=tk.Canvas(f_MHD0I01AV, width=50, height=130)
c.create_text(40, 60, text="MHD0I01AV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MHD0I01AV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MHD0I01AV)
slider.pack(side="top")

vv=epics.caget('DT:MHD0I01AV:BDL')
slider.set(vv)

def show_value_MBH0I01BV(val):
  # print(f"Current Value: {val} and name=MBH0I01BV:BDL")
  epics.caput('DT:MBH0I01BV:BDL',val)

f_MBH0I01BV=tk.Frame(root)
f_MBH0I01BV.pack(side="left")
c=tk.Canvas(f_MBH0I01BV, width=50, height=130)
c.create_text(40, 60, text="MBH0I01BV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH0I01BV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH0I01BV)
slider.pack(side="top")

vv=epics.caget('DT:MBH0I01BV:BDL')
slider.set(vv)

root.mainloop()