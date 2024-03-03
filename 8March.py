import tkinter as tk
import random as r
from time import sleep
def get_rgb(rgb):
    return '#%02x%02x%02x' % rgb

root = tk.Tk()
root.title("My Program")
canvas = tk.Canvas(root, width=600, height=600, bg="Magenta")
canvas.pack(padx=10, pady=10)
canvas.create_line (300 , 200 , 300 , 500 , fill="green")
canvas.create_oval(248, 50, 352, 202, fill="black")
canvas.create_oval(250, 50, 350, 200, fill="red")
canvas.create_oval(250, 50, 350, 142, fill="black")
canvas.create_oval(250, 50, 350, 140, fill="red")
canvas.create_oval(278, 78, 318, 108, fill="black")
canvas.create_oval(298, 248, 403, 302, fill="black")
canvas.create_oval(300, 250, 400, 300, fill="green")
canvas.create_oval(198, 252, 302, 302, fill="black")
canvas.create_oval(200, 250, 300, 300, fill="green")
canvas.create_text(300, 250, text="С праздником" ,font=('Comic Sans MS', 50), fill="pink")
for i in range(10000):
    x=r.randint(0,600)
    y=r.randint(0,600)
    canvas.create_oval(x, y,x+10,y+10, fill=get_rgb((r.randint(0,255),r.randint(0,255),r.randint(0,255))))
    root.update()
    sleep(0.1)
    

root.mainloop()
