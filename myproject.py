from tkinter import *


def queueprogram():
    import newqueueworking

def stackprogram():
    import StackWorking
root=Tk()
button1=Button(root,text="queue",command=queueprogram)
button2=Button(root,text="Stack",command=stackprogram)
button1.pack()
button2.pack()
