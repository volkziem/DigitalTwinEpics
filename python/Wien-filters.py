import tkinter as tk
import epics

root = tk.Tk()
root.title("Injector correctors H")
root.geometry("120x250")

def show_value_VWIEN(val):
  epics.caput('DT:V-WIEN:ANGLE',val)

f_VWIEN=tk.Frame(root)
f_VWIEN.pack(side="left")
c=tk.Canvas(f_VWIEN, width=50, height=130)
c.create_text(40, 60, text="V-WIEN angle", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_VWIEN, from_=90, to=-90, resolution=5,
   orient="vertical", command=show_value_VWIEN)
slider.pack(side="top")

vv=epics.caget('DT:V-WIEN:ANGLE')
slider.set(vv)

def show_value_HWIEN(val):
  epics.caput('DT:H-WIEN:ANGLE',val)

f_HWIEN=tk.Frame(root)
f_HWIEN.pack(side="left")
c=tk.Canvas(f_HWIEN, width=50, height=130)
c.create_text(40, 60, text="H-HIEN angle", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_HWIEN, from_=90, to=-90, resolution=5,
   orient="vertical", command=show_value_HWIEN)
slider.pack(side="top")

vv=epics.caget('DT:H-WIEN:ANGLE')
slider.set(vv)

root.mainloop()
