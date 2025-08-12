from tkinter import *
import time

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self, max_size):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size

    def isempty(self):
        return self.size == 0

    def isfull(self):
        return self.size == self.max_size

    def enqueue(self, data):
        if self.isfull():
            return "Overflow"
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        return True

    def dequeue(self):
        if self.isempty():
            return "Underflow"
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def peek_front(self):
        if self.isempty():
            return "Underflow"
        return self.front.data

    def peek_rear(self):
        if self.isempty():
            return "Underflow"
        return self.rear.data

    def display(self):
        result = []
        curr = self.front
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


class QueueLLApp(Frame):
    def __init__(self, master, obj):
        super().__init__(master)
        self.obj = obj
        self.pack(fill=BOTH, expand=True)
        self.colors = ["lightblue", "lightgreen", "orange", "yellow", "pink"]
        self.color_index = 0
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Queue (Linked List)", font=("Times", 20, "bold")).pack(pady=10)

        topframe = Frame(self)
        topframe.pack(side=TOP, pady=5)

        Label(topframe, text="Value:").grid(row=0, column=0, padx=5)
        self.entry = Entry(topframe, width=10)
        self.entry.grid(row=0, column=1, padx=5)
        Button(topframe, text="Enqueue", command=self.enqueue_value, bg="green", fg="white").grid(row=0, column=2, padx=5)

        Button(topframe, text="Dequeue", command=self.dequeue_value, bg="orange", fg="white").grid(row=1, column=0, padx=5)
        Button(topframe, text="Front", command=self.front_value, bg="blue", fg="white").grid(row=1, column=1, padx=5)
        Button(topframe, text="Rear", command=self.rear_value, bg="red", fg="white").grid(row=1, column=2, padx=5)
        Button(topframe, text="Display", command=self.display_queue, bg="purple", fg="white").grid(row=1, column=3, padx=5)

        self.canvas = Canvas(self, width=700, height=250, bg="white")
        self.canvas.pack(pady=10)

    def show_message(self, message):
        self.canvas.delete("msg")
        self.canvas.create_text(350, 20, text=message, font=("Arial", 12), fill="red", tags="msg")

    def enqueue_value(self):
        val = self.entry.get()
        if not val:
            return
        result = self.obj.enqueue(val)
        if result == "Overflow":
            self.show_message("Queue Overflow")
        else:
            self.entry.delete(0, END)
            self.show_message("")
            self.animate_enqueue(val)

    def dequeue_value(self):
        result = self.obj.dequeue()
        if result == "Underflow":
            self.show_message("Queue Underflow")
        else:
            self.show_message(f"Dequeued: {result}")
            self.animate_dequeue()

    def front_value(self):
        result = self.obj.peek_front()
        if result == "Underflow":
            self.show_message("Queue is Empty")
        else:
            self.show_message(f"Front: {result}")

    def rear_value(self):
        result = self.obj.peek_rear()
        if result == "Underflow":
            self.show_message("Queue is Empty")
        else:
            self.show_message(f"Rear: {result}")

    def display_queue(self):
        queue_items = self.obj.display()
        if not queue_items:
            self.show_message("Queue is Empty")
        else:
            self.show_message(f"Queue: {' -> '.join(map(str, queue_items))}")
        self.draw_queue()

    def draw_queue(self):
        self.canvas.delete("block")
        queue_items = self.obj.display()
        x, y = 50, 100
        for i, item in enumerate(queue_items):
            color = self.colors[i % len(self.colors)]
            self.canvas.create_rectangle(x, y, x+60, y+40, outline="black", fill=color, tags="block")
            self.canvas.create_text(x+30, y+20, text=item, tags="block")
            if i < len(queue_items)-1:
                self.canvas.create_line(x+60, y+20, x+80, y+20, arrow=LAST, tags="block")
            x += 80

    def animate_enqueue(self, val):
        rect = self.canvas.create_rectangle(700, 100, 760, 140, fill=self.colors[self.color_index], tags="block")
        text = self.canvas.create_text(730, 120, text=val, tags="block")
        x_pos = 700
        target_x = 50 + (self.obj.size-1) * 80
        while x_pos > target_x:
            self.canvas.move(rect, -5, 0)
            self.canvas.move(text, -5, 0)
            self.canvas.update()
            time.sleep(0.01)
            x_pos -= 5
        self.color_index = (self.color_index+1) % len(self.colors)
        self.draw_queue()

    def animate_dequeue(self):
        items = self.canvas.find_withtag("block")
        for _ in range(16):
            for item in items:
                self.canvas.move(item, -5, 0)
            self.canvas.update()
            time.sleep(0.01)
        self.draw_queue()


def open_window():
    win = Toplevel()
    win.title("Queue (Linked List)")
    win.geometry("800x400")
    QueueLLApp(win, QueueLL(5))



if __name__ == "__main__":
    root = Tk()
    QueueLLApp(root, QueueLL(5))
    root.mainloop()
