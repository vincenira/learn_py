class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        # calculating floor division which means integer return 
        # this is to have both element at 4th and 5th index have the same parent at 2nd index
        # To have also a left child at 2p index and the right child at 2p+1
        while i //2 >0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i //2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while (i *2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            # because the mc will calculate the subtree root or the root
            i = mc
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1 
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self, alist):
        # help to calculate the number of levels of the tree
        i = len(alist) // 2
        self.currentSize = len(alist)
        # the first element is zero to facilitate the division in operations.
        # and we concatenate it with the list alist
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1