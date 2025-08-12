from tkinter import *
import time

class Stack:
    def __init__(self):
        self.stack = []
        self.limit = 5

    def isempty(self):
        return len(self.stack) == 0

    def isfull(self):
        return len(self.stack) == self.limit

    def push(self, ele):
        if self.isfull():
            return "Overflow"
        self.stack.append(ele)
        return True

    def pop(self):
        if self.isempty():
            return "Underflow"
        return self.stack.pop()

    def peek(self):
        if self.isempty():
            return "Underflow"
        return self.stack[-1]

    def display(self):
        if self.isempty():
            return []
        return self.stack[::-1]  # top-first


class StackApp(Frame):
    def __init__(self, master, obj):
        super().__init__(master)
        self.obj = obj
        self.colors = ["lightblue", "lightgreen", "orange", "yellow", "pink"]
        self.color_index = 0
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Stack", font=("Times", 20, "bold")).pack(pady=10)

        topframe = Frame(self)
        topframe.pack(side=TOP, pady=5)

        Label(topframe, text="Push Value:").grid(row=0, column=0, padx=5)
        self.entry = Entry(topframe, width=10)
        self.entry.grid(row=0, column=1, padx=5)
        Button(topframe, text="Push", command=self.push_value, bg="green", fg="white").grid(row=0, column=2, padx=5)

        Button(topframe, text="Pop", command=self.pop_value, bg="orange", fg="white").grid(row=1, column=0, padx=5)
        Button(topframe, text="Peek", command=self.peek_value, bg="blue", fg="white").grid(row=1, column=1, padx=5)
        Button(topframe, text="Display", command=self.display_stack, bg="purple", fg="white").grid(row=1, column=2, padx=5)

        self.canvas = Canvas(self, width=300, height=350, bg="white")
        self.canvas.pack(pady=10)

    def show_message(self, message):
        self.canvas.delete("msg")
        self.canvas.create_text(150, 20, text=message, font=("Arial", 12), fill="red", tags="msg")

    def push_value(self):
        val = self.entry.get()
        if not val:
            return
        result = self.obj.push(val)
        if result == "Overflow":
            self.show_message("Stack Overflow")
        else:
            self.entry.delete(0, END)
            self.show_message("") 
            self.animate_push(val)

    def pop_value(self):
        result = self.obj.pop()
        if result == "Underflow":
            self.show_message("Stack Underflow")
        else:
            self.show_message(f"Popped: {result}")
            self.animate_pop()

    def peek_value(self):
        result = self.obj.peek()
        if result == "Underflow":
            self.show_message("Stack is Empty")
        else:
            self.show_message(f"Top: {result}")

    def display_stack(self):
        stack_items = self.obj.display()
        if not stack_items:
            self.show_message("Stack is Empty")
        else:
            self.show_message(f"Stack: {', '.join(map(str, stack_items))}")
        self.draw_stack()

    def draw_stack(self):
        self.canvas.delete("block")
        stack_items = self.obj.display()
        x1, y1 = 100, 300
        x2, y2 = 200, 350
        for i, item in enumerate(stack_items):
            color = self.colors[i % len(self.colors)]
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="block")
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=str(item), tags="block")
            y1 -= 50
            y2 -= 50

    def animate_push(self, val):
        y_start = 0
        y_end = 300 - (len(self.obj.stack)-1) * 50
        rect = self.canvas.create_rectangle(100, y_start, 200, y_start+50, fill=self.colors[self.color_index], tags="block")
        text = self.canvas.create_text(150, y_start+25, text=val, tags="block")
        while y_start < y_end:
            self.canvas.move(rect, 0, 5)
            self.canvas.move(text, 0, 5)
            self.canvas.update()
            time.sleep(0.01)
            y_start += 5
        self.color_index = (self.color_index+1) % len(self.colors)
        self.draw_stack()

    def animate_pop(self):
        items = self.canvas.find_withtag("block")
        if items:
            rect = items[-2]
            text = items[-1]
            for _ in range(20):
                self.canvas.move(rect, 0, -5)
                self.canvas.move(text, 0, -5)
                self.canvas.update()
                time.sleep(0.01)
            self.draw_stack()


def open_window():
    win = Toplevel()
    win.title("Stack")
    win.geometry("400x400")
    StackApp(win, Stack())
