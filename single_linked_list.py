from tkinter import *

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, max_size):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def insert_at_beginning(self, data):
        if self.size == self.max_size:
            return "Overflow"
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return True

    def insert_at_end(self, data):
        if self.size == self.max_size:
            return "Overflow"
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        return True

    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            return "Invalid position"
        if self.size == self.max_size:
            return "Overflow"
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
        return True

    def delete_from_beginning(self):
        if not self.head:
            return "Underflow"
        self.head = self.head.next
        self.size -= 1
        return True

    def delete_from_end(self):
        if not self.head:
            return "Underflow"
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        self.size -= 1
        return True

    def delete_at_position(self, position):
        if position < 0 or position >= self.size:
            return "Invalid position"
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
        return True

    def display(self):
        if not self.head:
            return []
        current = self.head
        data_list = []
        while current:
            data_list.append(str(current.data))
            current = current.next
        return data_list


class SinglyLinkedListApp:
    def __init__(self, root, max_size):
        self.root = root
        self.root.title("Singly Linked List")

        self.window_width = 900
        self.window_height = 500
        self.root.geometry(f"{self.window_width}x{self.window_height}")

        self.canvas = Canvas(self.root, width=850, height=350, bg="white")
        self.canvas.pack(pady=20)

        self.max_size = max_size
        self.linked_list = SinglyLinkedList(self.max_size)

        self.create_widgets()

    def create_widgets(self):
        self.input_frame = Frame(self.root, bg="lightblue", padx=20, pady=10)
        self.input_frame.pack(side=TOP, fill=X)

        self.data_label = Label(self.input_frame, text="Data:", font=("Arial", 12), bg="lightblue")
        self.data_label.grid(row=0, column=0, padx=5)

        self.data_entry = Entry(self.input_frame, font=("Arial", 12), width=10)
        self.data_entry.grid(row=0, column=1, padx=5)

        Button(self.input_frame, text="Insert Begin", command=self.insert_at_beginning, bg="green", fg="white").grid(row=0, column=2, padx=5)
        Button(self.input_frame, text="Insert End", command=self.insert_at_end, bg="green", fg="white").grid(row=0, column=3, padx=5)

        Label(self.input_frame, text="Pos:", font=("Arial", 12), bg="lightblue").grid(row=0, column=4, padx=5)
        self.pos_entry = Entry(self.input_frame, font=("Arial", 12), width=5)
        self.pos_entry.grid(row=0, column=5, padx=5)
        Button(self.input_frame, text="Insert Pos", command=self.insert_at_position, bg="green", fg="white").grid(row=0, column=6, padx=5)

        Button(self.input_frame, text="Del Begin", command=self.delete_from_beginning, bg="orange", fg="white").grid(row=1, column=2, padx=5)
        Button(self.input_frame, text="Del End", command=self.delete_from_end, bg="orange", fg="white").grid(row=1, column=3, padx=5)

        Label(self.input_frame, text="Pos:", font=("Arial", 12), bg="lightblue").grid(row=1, column=4, padx=5)
        self.del_pos_entry = Entry(self.input_frame, font=("Arial", 12), width=5)
        self.del_pos_entry.grid(row=1, column=5, padx=5)
        Button(self.input_frame, text="Del Pos", command=self.delete_at_position, bg="orange", fg="white").grid(row=1, column=6, padx=5)

        Button(self.input_frame, text="Display", command=self.display_list, bg="blue", fg="white").grid(row=2, column=3, padx=5)

    def show_message(self, msg):
        self.canvas.delete("msg")
        self.canvas.create_text(425, 20, text=msg, font=("Arial", 12), fill="red", tags="msg")

    def insert_at_beginning(self):
        data = self.data_entry.get().strip()
        if not data:
            self.show_message("Please enter data to insert.")
            return
        res = self.linked_list.insert_at_beginning(data)
        self.show_message("Inserted at beginning" if res is True else res)
        self.data_entry.delete(0, END)
        self.draw_linked_list()

    def insert_at_end(self):
        data = self.data_entry.get().strip()
        if not data:
            self.show_message("Please enter data to insert.")
            return
        res = self.linked_list.insert_at_end(data)
        self.show_message("Inserted at end" if res is True else res)
        self.data_entry.delete(0, END)
        self.draw_linked_list()

    def insert_at_position(self):
        data = self.data_entry.get().strip()
        pos = self.pos_entry.get().strip()
        if not data:
            self.show_message("Please enter data to insert.")
            return
        if not pos.isdigit():
            self.show_message("Please enter a valid non-negative integer position.")
            return
        pos = int(pos)
        if pos < 0 or pos > self.linked_list.size:
            self.show_message("Invalid position.")
            return
        res = self.linked_list.insert_at_position(data, pos)
        self.show_message(f"Inserted at pos {pos}" if res is True else res)
        self.data_entry.delete(0, END)
        self.pos_entry.delete(0, END)
        self.draw_linked_list()

    def delete_from_beginning(self):
        res = self.linked_list.delete_from_beginning()
        self.show_message("Deleted from beginning" if res is True else res)
        self.draw_linked_list()

    def delete_from_end(self):
        res = self.linked_list.delete_from_end()
        self.show_message("Deleted from end" if res is True else res)
        self.draw_linked_list()

    def delete_at_position(self):
        pos = self.del_pos_entry.get().strip()
        if not pos.isdigit():
            self.show_message("Please enter a valid non-negative integer position.")
            return
        pos = int(pos)
        if pos < 0 or pos >= self.linked_list.size:
            self.show_message("Invalid position.")
            return
        res = self.linked_list.delete_at_position(pos)
        self.show_message(f"Deleted at pos {pos}" if res is True else res)
        self.del_pos_entry.delete(0, END)
        self.draw_linked_list()

    def draw_node(self, x, y, data):
        node_width, node_height = 60, 40
        self.canvas.create_rectangle(x, y, x + node_width, y + node_height, outline="black", fill="lightblue", tags="list")
        self.canvas.create_text(x + node_width / 2, y + node_height / 2, text=data, font=("Arial", 12), tags="list")

    def draw_arrow(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, arrow=LAST, fill="black", width=2, tags="list")

    def draw_linked_list(self):
        self.canvas.delete("list")
        current = self.linked_list.head
        x, y = 100, 150
        while current:
            self.draw_node(x, y, current.data)
            if current.next:
                self.draw_arrow(x + 60, y + 20, x + 100, y + 20)
            x += 120
            current = current.next

    def display_list(self):
        data_list = self.linked_list.display()
        msg = " -> ".join(data_list) if data_list else "List is empty"
        self.show_message(msg)
        self.draw_linked_list()


def open_window():
    win = Toplevel()
    win.title("Singly Linked List")
    win.geometry("900x500")
    SinglyLinkedListApp(win, max_size=5)


if __name__ == "__main__":
    root = Tk()
    SinglyLinkedListApp(root, max_size=5)
    root.mainloop()
