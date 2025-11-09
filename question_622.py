class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0]*k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0        

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self):
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
