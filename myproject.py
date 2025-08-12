from tkinter import *


def queueprogram():
    import queueWorking

def stackprogram():
    import StackWorking

def linkedlistprogram():
    import single_linked_list
   
def stack_linkedlist():
    import stack_LL

def queue_linkedlist():
    import queue_LL

root=Tk()
button1=Button(root,text="queue",command=queueprogram)
button2=Button(root,text="Stack",command=stackprogram)
button3=Button(root,text="linkedlist",command=linkedlistprogram)
button4=Button(root,text="Stack_linkedlist",command=stack_linkedlist)
button5=Button(root,text="queue_linkedlist",command=queue_linkedlist)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()
