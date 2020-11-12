from tkinter import *
from time import sleep
from tkinter import messagebox

class Queue(Frame):
    def __init__(self,master):
        self.queue=list()
        self.rect=list()
        self.text=list()
        self.color=["light green","green","yellow","orange","red"]
        self.limit=5
        self.front=None
        self.rear=None
        super().__init__(master)
        self.pack()
        self.CreateWidget()
        
    def isfull(self):
        return len(self.queue) == self.limit

    def isempty(self):
        return len(self.queue) == 0

    def enqueuerect(self,rect,text,val):
        if self.enqueue(val):
           self.rect.append(rect)
           self.text.append(text)
        
    def enqueue(self,val):
        if self.isfull():
            messagebox.showwarning("Warning","Queue Overflow")
            return False

        else:
            if self.front==None and self.rear==None:
                self.front=self.rear=0
            else:
                self.rear+=1
            self.queue.append(val)
            return True

    def dequeuerect(self):
        if self.dequeue():
          self.rect.pop(0)
          self.text.pop(0)
           
    def dequeue(self):
        if self.isempty():
            messagebox.showwarning("Warning","Queue Underflow")
            return False

        else:
            if self.front == self.rear :
                   self.front=self.rear=None
            else:
                self.front+=1
            self.queue.pop(0)
            return True

    def display(self):
        if self.isempty():
            messagebox.showwarning("Warning","Queue Underflow")
        else:
           print(self.queue)

    def CreateWidget(self):
       Label(self,text="Working of Queue",font=("Times",20,"bold")).pack()
     
       self.topframe=Frame(self,bg="Light Green",height=150,width=500)
       self.topframe.pack(side=TOP)

       self.bottomframe=Frame(self,height=350,width=500)
       self.bottomframe.pack(side=BOTTOM,fill=BOTH,expand=1)

       self.create=Button(self.topframe,text="Create Queue",command=self.createqueue)
       self.create.grid(row=0,column=0,sticky=NW)
       self.push=Label(self.topframe,text="Enqueue")
       self.push.grid(row=1,column=0,sticky=NE)
       self.entry1=Entry(self.topframe,width=8)
       self.entry1.grid(row=1,column=1)
       self.accept=Button(self.topframe,text="accept",command=self.pushvalue)
       self.accept.grid(row=1,column=3)

       self.pop = Button(self.topframe,text="dequeue",command=self.popvalue)
       self.pop.grid(row=2,column=0)

       
       self.display=Button(self.topframe,text="Display",command=self.display)
       self.display.grid(row=2,column=5)

       self.c = Canvas(self.bottomframe,height=350,width=400,bg="pink")
       self.c.pack()
       
    def createqueue(self):
        
        self.create.config(text="Delete Queue",command=self.deletequeue)
        self.c.create_line(50,100,300,100)
        self.c.create_line(50,250,300,250)
        self.x1,self.y1,self.x2,self.y2 = 50,100,100,250
        self.c_index=-1
        
    def deletequeue(self):
        self.c.delete("all")
        self.create.config(text="Create Queue",command=self.createqueue)
        self.queue=[]

    def switchAllButtons(self):
        self.switchAcceptButton()
        self.switchPopButton()
        
    def switchAcceptButton(self):
        if self.accept["state"] == "normal":
            self.accept["state"] = "disabled"
        else:
            self.accept["state"] = "normal"
    def switchPopButton(self):
        if self.pop["state"] == "normal":
            self.pop["state"] = "disabled"
        else:
            self.pop["state"] = "normal"


    def pushvalue(self):
        self.switchAllButtons()
        val=self.entry1.get()
    
        if val== "":
            return
        elif not self.isfull():
            
            if self.c_index == len(self.color)-1 :
              self.c_index=0
            else:
              self.c_index+=1
              
         
            rect=self.c.create_rectangle(400,100,450,250,fill=self.color[self.c_index])
            
            text=self.c.create_text(430,150,text=val,justify=CENTER,font=("Times",20,'bold'))
                      
            self.enqueuerect(rect,text,val)
                     
            self.moveelements()
            
            self.x1,self.x2 = self.x1+50,self.x2+50   #changing the coordinates

            
        else:
            messagebox.showwarning("Warning","Queue OverFlow")

        
        self.entry1.delete(0,END)
        self.switchAllButtons()
        
    def popvalue(self):
        self.switchAllButtons()

        self.x1,self.x2 = self.x1-50,self.x2-50
        xend=0
        for i in range(len(self.rect)):
    
            while True :

                self.c.move(self.rect[i],-5,0)
                self.c.move(self.text[i],-5,0)
                pos=self.c.coords(self.rect[i])
                sleep(0.02)
                self.c.update()
                if pos[2]== xend :
                    # the second block need to be moved to the first position
                    if i!=0 :
                        xend+=50     
                    else:
                        xend+=100      
                    sleep(0.1)
                    break      

        self.dequeuerect()
        self.switchAllButtons()
        
    def moveelements(self):                                
           while True :
                self.c.move(self.rect[len(self.queue)-1],-5,0)
                self.c.move(self.text[len(self.queue)-1],-5,0)
                pos=self.c.coords(self.rect[len(self.queue)-1])
                sleep(0.005)
                self.c.update()
                if pos[0]==self.x1:
                    break

root=Tk()
root.title("Working of Queue")
root.geometry("500x500")

app=Queue(root)
root.mainloop()



























           
            
