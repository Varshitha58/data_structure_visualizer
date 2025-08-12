from tkinter import *
import time

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self, max_size):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.max_size

    def push(self, data):
        if self.is_full():
            return "Overflow"
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True

    def pop(self):
        if self.is_empty():
            return "Underflow"
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            return "Underflow"
        return self.top.data

    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class StackApp(Frame):
    def __init__(self, master, obj):
        super().__init__(master)
        self.obj = obj
        self.colors = ["lightblue", "lightgreen", "orange", "yellow", "pink"]
        self.color_index = 0
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Stack (Linked List Style)", font=("Times", 20, "bold")).pack(pady=10)

        topframe = Frame(self)
        topframe.pack(side=TOP, pady=5)

        Label(topframe, text="Push Value:").grid(row=0, column=0, padx=5)
        self.entry = Entry(topframe, width=10)
        self.entry.grid(row=0, column=1, padx=5)
        Button(topframe, text="Push", command=self.push_value, bg="green", fg="white").grid(row=0, column=2, padx=5)

        Button(topframe, text="Pop", command=self.pop_value, bg="orange", fg="white").grid(row=1, column=0, padx=5)
        Button(topframe, text="Peek", command=self.peek_value, bg="blue", fg="white").grid(row=1, column=1, padx=5)
        Button(topframe, text="Display", command=self.display_stack, bg="purple", fg="white").grid(row=1, column=2, padx=5)

        self.canvas = Canvas(self, width=350, height=400, bg="white")
        self.canvas.pack(pady=10)

    def show_message(self, message):
        self.canvas.delete("msg")
        self.canvas.create_text(175, 20, text=message, font=("Arial", 12), fill="red", tags="msg")

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

        if not stack_items:
            return

        x = 160  
        y = 60  

        for i, item in enumerate(stack_items):
            self.canvas.create_rectangle(x-40, y, x+40, y+50,
                                        fill=self.colors[i % len(self.colors)], tags="block")
            self.canvas.create_text(x, y+25, text=str(item), tags="block")

            if i < len(stack_items) - 1:
                self.canvas.create_line(x, y+50, x, y+70, arrow=LAST, tags="block")
            y += 70

    def animate_push(self, val):
        items = self.canvas.find_withtag("block")
        for _ in range(12):
            for item in items:
                self.canvas.move(item, 0, 5)
            self.canvas.update()
            time.sleep(0.01)
        self.canvas.create_rectangle(120, 60, 200, 110, fill=self.colors[self.color_index], tags="block")
        self.canvas.create_text(160, 85, text=val, tags="block")
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.draw_stack()

    def animate_pop(self):
        items = self.canvas.find_withtag("block")
        if not items:
            return

        rect = items[0]
        text = items[1]

        for _ in range(12):
            self.canvas.move(rect, 0, -5)
            self.canvas.move(text, 0, -5)
            self.canvas.update()
            time.sleep(0.01)

        self.canvas.delete(rect)
        self.canvas.delete(text)

        self.draw_stack()



def open_window():
    win = Toplevel()
    win.title("Stack (Linked List Style)")
    win.geometry("400x450")
    StackApp(win, StackLL(5))


if __name__ == "__main__":
    root = Tk()
    StackApp(root, StackLL(5))
    root.mainloop()
