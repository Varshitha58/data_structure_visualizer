from tkinter import *
import importlib

def load_window(module_name):
    try:
        mod = importlib.import_module(module_name)
        importlib.reload(mod)  
        mod.open_window()     
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except AttributeError:
        print(f"Error: 'open_window()' not found in {module_name}.")

root = Tk()
root.title("Data Structures Visualizer")
root.geometry("700x700+200+200")
root.configure(bg="black")

Label(
    root, 
    text="DATA STRUCTURES", 
    font=("Helvetica", 30), 
    bg="black", 
    fg="red"
).pack(pady=20)

Button(
    root, text="Stack", height=2, width=30, 
    font=("Arial black", 13), command=lambda: load_window("StackWorking")
).place(x=150, y=100)

Button(
    root, text="Queue", height=2, width=30, 
    font=("Arial black", 13), command=lambda: load_window("queueWorking")
).place(x=150, y=200)

Button(
    root, text="Linked List", height=2, width=30, 
    font=("Arial black", 13), command=lambda: load_window("single_linked_list")
).place(x=150, y=300)

Button(
    root, text="Stack (Linked List)", height=2, width=30, 
    font=("Arial black", 13), command=lambda: load_window("stack_LL")
).place(x=150, y=400)

Button(
    root, text="Queue (Linked List)", height=2, width=30, 
    font=("Arial black", 13), command=lambda: load_window("queue_LL")
).place(x=150, y=500)

root.mainloop()
