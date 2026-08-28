# adjust correctors in digital twin, V. Ziemann, 260813
import tkinter as tk
import epics

name='LH:MBH2I00AV'

def show_value1(val):
    print(f"Current Value: {val}    and name: {name}")
    epics.caput(name,val)

vv=epics.caget(name)
print(f" value is {vv}")
    
root = tk.Tk()
root.title(name)
root.geometry("100x250")

ff=tk.Frame(root)
ff.pack(side="left")

c=tk.Canvas(ff, width=50, height=130)
c.create_text(40, 60, text=name, angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")

slider = tk.Scale(ff, from_=10, to=-10, resolution=0.1,
                  orient="vertical", command=show_value1)
slider.pack(side="top")
slider.set(vv)

root.mainloop()
    
