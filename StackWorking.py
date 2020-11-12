from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Stack():
    def __init__(self):
        self.stack=[]
        self.limit=5
        self.top=0
        
    def isempty(self):
        return len(self.stack) == 0
    def isfull(self):
        return len(self.stack)== self.limit
    
    def push(self,ele):
        if self.isfull():
            messagebox.showwarning("Warning","Stack Overflow")
        else:
            self.stack.append(ele)
            self.top+=1

    def pop(self):
        if self.isempty():
            messagebox.showwarning("Warning","Stack Underflow")

        else:
            self.stack.pop()
            self.top-=1

    def peek(self):
        if self.isempty():
            messagebox.showwarning("Warning","Stack Underflow")
        else:
            return self.stack[-1]
            
    def display(self):
         for i in self.stack:
             print(i,end=" ")

             
class Application(Frame):

    def __init__(self,master,obj):
     super().__init__(master)
     self.obj=obj
     self.pack()
     
     self.CreateWidget()

    def CreateWidget(self):
       Label(self,text="Working of Stack",font=("Times",20,"bold")).pack()
     
       self.topframe=Frame(self,bg="Light Green",height=150,width=500)
       self.topframe.pack(side=TOP,fill=BOTH,expand=1)

       self.bottomframe=Frame(self,height=350,width=500)
       self.bottomframe.pack(side=BOTTOM,fill=BOTH,expand=1)

       ttk.Separator(root,orient=HORIZONTAL).pack()
       
       self.create=Button(self.topframe,text="Create Stack",command=self.createstack)
       self.create.grid(row=0,column=2,columnspan=5,sticky=NW)
       self.push=Label(self.topframe,text="Push")
       self.push.grid(row=1,column=1,sticky=NE,pady=3)
       self.entry1=Entry(self.topframe,width=8)
       self.entry1.grid(row=1,column=2)
       self.accept=Button(self.topframe,text="accept",command=self.pushvalue)
       self.accept.grid(row=1,column=3,pady=3)

       self.pop=Button(self.topframe,text="Pop",command=self.popvalue)
       self.pop.grid(row=2,column=0)

       self.peek=Button(self.topframe,text="Peek",command=self.peekvalue)
       self.peek.grid(row=2,column=2)
       
       self.display=Button(self.topframe,text="Display",command=self.obj.display)
       self.display.grid(row=2,column=5)

       self.c=Canvas(self.bottomframe,height=350,width=400,bg="pink")
       self.c.pack()


    def createstack(self):
        
        self.c.create_line(100,50,100,300)
        self.c.create_line(100,300,250,300)
        self.c.create_line(250,300,250,50)
        self.create.config(text="Delete Stack",command=self.deletestack)
        self.x1,self.y1,self.x2,self.y2 = 100,250,250,300
        self.rect=[None for i in range(5)]         #5 boxes inside the stack
        self.text=[None for i in range(5)]    
        self.irect=-1
        self.trect=-1
        self.color=["light green","green","yellow","orange","red"]
        self.c_index=0

    def deletestack(self):
        self.c.delete("all")
        self.create.config(text="Create Stack",command=self.createstack)
        

    def pushvalue(self):
        val=self.entry1.get()
        if val== "":
            return
        elif not self.obj.isfull():
            self.obj.push(val)
            self.irect+=1
            self.trect+=1
            self.rect[self.irect] =self.c.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill=self.color[self.c_index])
            self.text[self.trect]=self.c.create_text(self.x1+60,self.y1+20,text=val,justify=CENTER,font=("Times",20,'bold'))
            self.x1,self.y1,self.x2,self.y2 = self.x1,self.y1-50,self.x2,self.y2-50
            if self.c_index == len(self.color)-1 :
              self.c_index=0
            else:
              self.c_index+=1
        else:
            messagebox.showwarning("Warning","Stack OverFlow")

        
        self.entry1.delete(0,END)

    
    def popvalue(self):
        self.obj.pop()
        self.c.delete(self.rect[self.irect])
        self.c.delete(self.text[self.trect])
        self.x1,self.y1,self.x2,self.y2 = self.x1,self.y1+50,self.x2,self.y2+50
        self.irect-=1
        self.trect-=1

    def peekvalue(self):
    
        self.c.itemconfig(self.rect[self.irect],fill="GOLD")   #use  canvas.itemconfig(canvasobject,options)
        print(self.obj.peek())
        
           
              
root=Tk()
root.title("Data Structure")
root.geometry("500x500")
s=Stack()
App=Application(root,s)
root.mainloop()
