class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue=[]
        self.size=k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if(self.isFull()):
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if(self.isEmpty()):
            return False
        else:
            del self.queue[0]
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if(not self.isEmpty()):
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if(not self.isEmpty()):
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if(self.queue==[]):
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if(len(self.queue)==self.size):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

#比较标准的版本
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue=[0]*k
        self.head=-1
        self.tail=-1
        self.size=k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if(self.isFull()):
            return False
        else:
            if(self.head==-1):
                self.head+=1
            self.tail+=1
            self.tail%=self.size
            self.queue[self.tail]=value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if(self.isEmpty()):
            return False
        else:
            if(self.head==self.tail):
                self.queue[self.head]=0
                self.head=-1
                self.tail=-1
            else:
                self.queue[self.head]=0
                self.head+=1
                self.head%=self.size
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if(not self.isEmpty()):
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if(not self.isEmpty()):
            return self.queue[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if(self.head==-1):
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if(self.tail-self.head==self.size-1 or self.head-self.tail==1):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()