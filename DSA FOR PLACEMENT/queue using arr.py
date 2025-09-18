from collections import deque
q = deque()
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def isempty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

pq = Queue()
pq.enqueue({
    
})

