from tkinter import *

def stack():
    import StackWorking

def queue():
     import newqueueworking

root=Tk()
root.geometry("600x600+200+200")
Label(root,text="DATA VISUALIZATION ",font=("Helvetica",30),bg="Black",fg="RED").pack()


Button(root,text="Stack Working",height = "2", width = "30",font = ("Arial black",13),command=stack).place(x=150,y=200)

Button(root,text="Queue Working",height = "2", width = "30",font = ("Arial black",13),command=queue).place(x=150,y=300)


