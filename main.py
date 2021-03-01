import tkinter 
from tkinter import *
from tkinter.ttk import *
from time import strftime

master=tkinter.Tk()
master.title("Digital clock")
label = Label(master,font=("calibri",40,'bold'),background = 'Blue', foreground='White')

def time():
  string=strftime("%H:%M:%S %p")
  label.config(text=string)
  label.after(1000,time)

label.pack(anchor='center')
time()

master.mainloop()