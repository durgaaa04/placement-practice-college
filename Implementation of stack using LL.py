class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def Push(self, newdata):
        newnode = Node(newdata)
        if self.top == None:
            self.top = newnode
        else:
            newnode.next = self.top 
            self.top = newnode
    
    def Pop(self):
        if self.top == None:
            self.top = newnode
        else:
            self.top = self.top.next
    
    def Peek(self):
        if self.top == None:
            print("stack is empty")
        else:
            print(self.top.data)

    def Display(self):
        temp = self.top
        while temp:
            print(str(temp.data), end = " ")
            temp = temp.next

if __name__ == "__main__":
    s = Stack()
    s.Push(1)
    s.Push(2)
    s.Push(3)
    s.Push(4)
    s.Push(5)
    s.Pop()
    s.Peek()
    s.Display()

