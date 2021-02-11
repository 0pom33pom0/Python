"""
p = {}
for i in range(2):
    x = input("")
    y = input("")
    p[y]="{0:-<15}".format(x)
print(p)
"""
import tkinter as tk

window = tk.Tk()
window.title("pom")
window.minsize(width = 400,height = 400)

p = tk.Label(master=window,text="pom")
p.pack()

window.mainloop()