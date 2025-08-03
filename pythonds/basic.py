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
        return len(self.items)

    def __str__(self):
         return f"{self.items}"

class Stack2:
    def __init__(self, name):
       self.name = name 
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
        return len(self.items)

    def __str__(self):
         return f"{self.items}"

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
    def __str__(self):
         return f"{self.items}"

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

    def __str__(self):
         return f"{self.items}"

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


class Node:
    def __init__(self, initialData):
        self.data = initialData
        self.next = None

    def getData(self):
        return self.data

    def getNextData(self):
        return self.next
        
    def setData(self, data):
        self.data = data

    def setNextData(self, nextData):
        self.next = nextData

class BaseList:
    def __init__(self):
        self.head = None
        self.queue = None
        self.number_of_elts = 0
    
    def __str__(self):
        items = "["
        separator = ", "
        current = self.head
        while None != current:
            item = current.getData()
            items += f"{item}"
            if None != current.getNextData():
                items += ", " 
            current = current.getNextData()
        items += "]"
        return items
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current.getNextData() != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNextData()
        if found:
            if self.head == None:
                self.head = current.getNextData()
            else:
                previous.setNextData(current.getNextData())
            if self.number_of_elts > 0:
                self.number_of_elts -=1
    
    def search(self, item):
        current = self.head
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else: 
                current = current.getNextData()
        return found
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNextData()
        return count

    def sizeL(self):
        return self.number_of_elts

    def isEmpty(self):
        return self.head == None
        
    def index(self, item):
        current = self.head
        count = 0
        while current.getData() != item and current != None:
            current = current.getNextData()
            count = count + 1
        return count
    def pop(self):
        current = self.head
        previous = None
        while current.getNextData() != None:
            previous = current
            current = current.getNextData()
        result = previous.getData()
        if self.head == None:
            self.head = current.getNextData()
        else:
            previous.setNextData(current.getNextData())
            if self.number_of_elts > 0:
                self.number_of_elts -=1
        return result
        
    def popPos(self, pos):
        current = self.head
        previous = None
        count = 0
        position = pos
        while count != position and current.getNextData() != None:
            previous = current
            current = current.getNextData()
            count = count + 1
        result = previous.getData()
        if self.head == None:
            self.head = current.getNextData()
        else:
            previous.setNextData(current.getNextData())
            if self.number_of_elts > 0:
                self.number_of_elts -=1
        return result

    def slice(self, start, stop):
        current = self.head
        count = 0
        new_list = BaseList() 

        if start < stop:
            while start != count:
                current = current.getNextData()
                count += 1
            while count < stop:
                new_list.add(current.getData())
                current = current.getNextData()
                count += 1
            return new_list