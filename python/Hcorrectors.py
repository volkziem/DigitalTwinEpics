import tkinter as tk
import epics

root = tk.Tk()
root.title("Injector correctors H")
root.geometry("700x250")

def show_value_MBH2I00H(val):
  # print(f"Current Value: {val} and name=MBH2I00H:BDL")
  epics.caput('DT:MBH2I00H:BDL',val)

f_MBH2I00H=tk.Frame(root)
f_MBH2I00H.pack(side="left")
c=tk.Canvas(f_MBH2I00H, width=50, height=130)
c.create_text(40, 60, text="MBH2I00H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I00H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I00H)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I00H:BDL')
slider.set(vv)

def show_value_MBH2I00AH(val):
  # print(f"Current Value: {val} and name=MBH2I00AH:BDL")
  epics.caput('DT:MBH2I00AH:BDL',val)

f_MBH2I00AH=tk.Frame(root)
f_MBH2I00AH.pack(side="left")
c=tk.Canvas(f_MBH2I00AH, width=50, height=130)
c.create_text(40, 60, text="MBH2I00AH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I00AH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I00AH)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I00AH:BDL')
slider.set(vv)

def show_value_MBH2I01H(val):
  # print(f"Current Value: {val} and name=MBH2I01H:BDL")
  epics.caput('DT:MBH2I01H:BDL',val)

f_MBH2I01H=tk.Frame(root)
f_MBH2I01H.pack(side="left")
c=tk.Canvas(f_MBH2I01H, width=50, height=130)
c.create_text(40, 60, text="MBH2I01H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I01H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I01H)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I01H:BDL')
slider.set(vv)

def show_value_MBH2I01AH(val):
  # print(f"Current Value: {val} and name=MBH2I01AH:BDL")
  epics.caput('DT:MBH2I01AH:BDL',val)

f_MBH2I01AH=tk.Frame(root)
f_MBH2I01AH.pack(side="left")
c=tk.Canvas(f_MBH2I01AH, width=50, height=130)
c.create_text(40, 60, text="MBH2I01AH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH2I01AH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH2I01AH)
slider.pack(side="top")

vv=epics.caget('DT:MBH2I01AH:BDL')
slider.set(vv)

def show_value_MBH1I02H(val):
  # print(f"Current Value: {val} and name=MBH1I02H:BDL")
  epics.caput('DT:MBH1I02H:BDL',val)

f_MBH1I02H=tk.Frame(root)
f_MBH1I02H.pack(side="left")
c=tk.Canvas(f_MBH1I02H, width=50, height=130)
c.create_text(40, 60, text="MBH1I02H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I02H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I02H)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I02H:BDL')
slider.set(vv)

def show_value_MBH1I03H(val):
  # print(f"Current Value: {val} and name=MBH1I03H:BDL")
  epics.caput('DT:MBH1I03H:BDL',val)

f_MBH1I03H=tk.Frame(root)
f_MBH1I03H.pack(side="left")
c=tk.Canvas(f_MBH1I03H, width=50, height=130)
c.create_text(40, 60, text="MBH1I03H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I03H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I03H)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I03H:BDL')
slider.set(vv)

def show_value_MBH1I04H(val):
  # print(f"Current Value: {val} and name=MBH1I04H:BDL")
  epics.caput('DT:MBH1I04H:BDL',val)

f_MBH1I04H=tk.Frame(root)
f_MBH1I04H.pack(side="left")
c=tk.Canvas(f_MBH1I04H, width=50, height=130)
c.create_text(40, 60, text="MBH1I04H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I04H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I04H)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I04H:BDL')
slider.set(vv)

def show_value_MBH1I05H(val):
  # print(f"Current Value: {val} and name=MBH1I05H:BDL")
  epics.caput('DT:MBH1I05H:BDL',val)

f_MBH1I05H=tk.Frame(root)
f_MBH1I05H.pack(side="left")
c=tk.Canvas(f_MBH1I05H, width=50, height=130)
c.create_text(40, 60, text="MBH1I05H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I05H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I05H)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I05H:BDL')
slider.set(vv)

def show_value_MBH1I07H(val):
  # print(f"Current Value: {val} and name=MBH1I07H:BDL")
  epics.caput('DT:MBH1I07H:BDL',val)

f_MBH1I07H=tk.Frame(root)
f_MBH1I07H.pack(side="left")
c=tk.Canvas(f_MBH1I07H, width=50, height=130)
c.create_text(40, 60, text="MBH1I07H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH1I07H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH1I07H)
slider.pack(side="top")

vv=epics.caget('DT:MBH1I07H:BDL')
slider.set(vv)

def show_value_MBH0I01H(val):
  # print(f"Current Value: {val} and name=MBH0I01H:BDL")
  epics.caput('DT:MBH0I01H:BDL',val)

f_MBH0I01H=tk.Frame(root)
f_MBH0I01H.pack(side="left")
c=tk.Canvas(f_MBH0I01H, width=50, height=130)
c.create_text(40, 60, text="MBH0I01H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH0I01H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH0I01H)
slider.pack(side="top")

vv=epics.caget('DT:MBH0I01H:BDL')
slider.set(vv)

def show_value_MHD0I01AH(val):
  # print(f"Current Value: {val} and name=MHD0I01AH:BDL")
  epics.caput('DT:MHD0I01AH:BDL',val)

f_MHD0I01AH=tk.Frame(root)
f_MHD0I01AH.pack(side="left")
c=tk.Canvas(f_MHD0I01AH, width=50, height=130)
c.create_text(40, 60, text="MHD0I01AH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MHD0I01AH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MHD0I01AH)
slider.pack(side="top")

vv=epics.caget('DT:MHD0I01AH:BDL')
slider.set(vv)

def show_value_MBH0I01BH(val):
  # print(f"Current Value: {val} and name=MBH0I01BH:BDL")
  epics.caput('DT:MBH0I01BH:BDL',val)

f_MBH0I01BH=tk.Frame(root)
f_MBH0I01BH.pack(side="left")
c=tk.Canvas(f_MBH0I01BH, width=50, height=130)
c.create_text(40, 60, text="MBH0I01BH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBH0I01BH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBH0I01BH)
slider.pack(side="top")

vv=epics.caget('DT:MBH0I01BH:BDL')
slider.set(vv)

root.mainloop()