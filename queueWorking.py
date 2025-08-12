from tkinter import *
import time

class Queue:
    def __init__(self, limit = 5):
        self.queue = []
        self.limit = limit

    def isempty(self):
        return len(self.queue) == 0

    def isfull(self):
        return len(self.queue) == self.limit

    def enqueue(self, val):
        if self.isfull():
            return "Overflow"
        self.queue.append(val)
        return True

    def dequeue(self):
        if self.isempty():
            return "Underflow"
        return self.queue.pop(0)

    def front(self):
        if self.isempty():
            return "Underflow"
        return self.queue[0]
    
    def rear(self):
        if self.isempty():
            return "Underflow"
        return self.queue[-1]

    def display(self):
        return self.queue[:]  


class QueueApp(Frame):
    def __init__(self, master, obj):
        super().__init__(master)
        self.obj = obj
        self.colors = ["lightblue", "lightgreen", "orange", "yellow", "pink"]
        self.color_index = 0
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Queue (Array)", font=("Times", 20, "bold")).pack(pady=10)

        topframe = Frame(self)
        topframe.pack(side=TOP, pady=5)

        Label(topframe, text="Enqueue Value:").grid(row=0, column=0, padx=5)
        self.entry = Entry(topframe, width=10)
        self.entry.grid(row=0, column=1, padx=5)
        Button(topframe, text="Enqueue", command=self.enqueue_value, bg="green", fg="white").grid(row=0, column=2, padx=5)

        Button(topframe, text="Dequeue", command=self.dequeue_value, bg="orange", fg="white").grid(row=1, column=0, padx=5)
        Button(topframe, text="Front", command=self.front_value, bg="blue", fg="white").grid(row=1, column=1, padx=5)
        Button(topframe, text="Rear", command=self.rear_value, bg="red", fg="white").grid(row=1, column=2, padx=5)
        Button(topframe, text="Display", command=self.display_queue, bg="purple", fg="white").grid(row=1, column=3, padx=5)

        self.canvas = Canvas(self, width=500, height=200, bg="white")
        self.canvas.pack(pady=10)

    def show_message(self, message):
        self.canvas.delete("msg")
        self.canvas.create_text(250, 20, text=message, font=("Arial", 12), fill="red", tags="msg")

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
        result = self.obj.front()
        if result == "Underflow":
            self.show_message("Queue is Empty")
        else:
            self.show_message(f"Front: {result}")

    def rear_value(self):
        result = self.obj.rear()
        if result == "Underflow":
            self.show_message("Queue is Empty")
        else:
            self.show_message(f"Rear: {result}")

    def display_queue(self):
        queue_items = self.obj.display()
        if not queue_items:
            self.show_message("Queue is Empty")
        else:
            self.show_message(f"Queue: {', '.join(map(str, queue_items))}")
        self.draw_queue()

    def draw_queue(self):
        self.canvas.delete("block")
        queue_items = self.obj.display()
        x1, y1 = 50, 80
        x2, y2 = 100, 130
        for i, item in enumerate(queue_items):
            color = self.colors[i % len(self.colors)]
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="block")
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=str(item), tags="block")
            x1 += 60
            x2 += 60

    def animate_enqueue(self, val):
        rect = self.canvas.create_rectangle(500, 80, 550, 130, fill=self.colors[self.color_index], tags="block")
        text = self.canvas.create_text(525, 105, text=val, tags="block")
        x_pos = 500
        target_x = 50 + (len(self.obj.queue)-1) * 60
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
        for _ in range(12):
            for item in items:
                self.canvas.move(item, -5, 0)
            self.canvas.update()
            time.sleep(0.01)
        self.draw_queue()


def open_window():
    win = Toplevel()
    win.title("Queue (Array)")
    win.geometry("600x300")
    QueueApp(win, Queue())

if __name__ == "__main__":
    root = Tk()
    QueueApp(root, Queue(5))
    root.mainloop()

