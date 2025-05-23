class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def InsertionAtBeginning(self, newdata):
        newnode = Node(newdata)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def InsertionAtEnd(self,newdata):
        newnode = Node(newdata)
        if self.head == None:
            self.head = newnode
        else:
            Last = self.head
            while Last.next != None:
                Last = Last.next
            Last.next = newnode

    def InsertionAtAnyPosition(self, newdata, pos):
        newnode = Node(newdata)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            for i in range(1, pos - 1):
                temp = temp.next
                newnode.next = temp.next
                temp.next = newnode

    def DeletionAtBeginning(self):
        if self.head == None:
            print("llist is empty")
        else:
            self.head = self.head.next

    def DeletionAtEnd(self):
        if self.head == None:
            print("llist is empty")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    def search(self, key):
        temp = self.head
        while temp:
            if (temp.data == key):
                print(temp.data, "is found")
                break
            temp = temp.next

    def sorting(self):
        if(self.head == None):
            print("llist is empty")
        else:
            curr = self.head
            while curr:
                Index = curr.next
                while Index:
                    if(curr.data > Index.data):
                        curr.data, Index.data = Index.data, curr.data 
                    Index = Index.next
                curr = curr.next   


    def printlist(self):
        temp = self.head
        while(temp):
            print(str(temp.data) + " ", end = " ")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.InsertionAtBeginning(3)
    llist.InsertionAtBeginning(8)
    llist.InsertionAtEnd(5)
    llist.InsertionAtAnyPosition(7,3)
    print("without sorting:")
    llist.printlist()
    print("\nwith sorting:")
    llist.sorting()
    llist.printlist()


