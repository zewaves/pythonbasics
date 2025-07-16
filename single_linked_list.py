class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    def display(self):
        if self.head == None:
            print("Empty List")
            return
        current = self.head
        while current.next:
            print(current.data, sep= "", end=" ")
            current = current.next
        print(current.data)
    def insert_front(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        previousfront = self.head
        self.head = newnode
        newnode.next = previousfront
    def insert_after(self, prev, data):
        current = self.head
        while current:
            if current.data == prev:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        print(f"{prev} not found")

L1 = LinkedList()
L1.insert_end(10)
L1.insert_end(20)
L1.insert_end(30)
L1.insert_front(00)
L1.insert_after(20, 25)
L1.display()