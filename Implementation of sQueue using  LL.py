class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.top = None
    
    def enqueue(self, newdata):
        newnode = Node(newdata)
        if self.top == None:
            self.top = newnode
        else:
            Last = self.top
            while Last.next != None:
                Last = Last.next
            Last.next = newnode
    
    def dequeue(self):
        if self.top == None:
            print("Queue is empty")
        else:
            self.top = self.top.next
    
    def Display(self):
        temp = self.top
        while temp:
            print(str(temp.data), end = " ")
            temp = temp.next

if __name__ == "__main__":
    quit = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    s.dequeue()
    s.Display()

