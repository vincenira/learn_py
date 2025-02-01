class Stack:
    def __init__(self):
       self.items = []
        
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        return self.items == []
        
    def peek(self):
        length = len(self.items)
        if length > 0:
            return self.items[length - 1]
        return []
        
    def size(self):
        return len(self.stack)
    

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Queue2:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def dequeue(self):
        self.items.pop(0)

    def enqueue(self, item):
        return self.items.append(item)

    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        return self.items.append(item)
        
    def addRear(self, item):
        return self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []