import sys
from tkinter import *
import time

def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,timing)

root=Tk()
root.geometry("600x300")
clock=Label(root,font=("times",60,"bold"),bg="lavender")
clock.grid(row=2,column=2,pady=30,padx=100)
timing()

digital=Label(root,text="Bhargavi's Digital clock",font="times 25 bold")
digital.grid(row=0,column=2)

nota=Label(root,text="    Hours        Minutes        Seconds     ",font="times 16 bold")
nota.grid(row=3,column=2)

root.mainloop()