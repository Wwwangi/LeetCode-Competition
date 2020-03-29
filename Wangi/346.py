import queue

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.q=queue.Queue(size)

    def next(self, val: int) -> float:
        if(self.q.full()):
            self.q.get()
        self.q.put(val)
        temp=0
        for num in list(self.q.queue):
            temp+=num
        temp/=self.q.qsize()
        return temp


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


#无循环，time complexity好一些
import queue

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.q=queue.Queue(size)
        self.total=0

    def next(self, val: int) -> float:
        if(self.q.full()):
            temp=self.q.get()
            self.total-=temp
        self.q.put(val)
        self.total+=val
        res=self.total/self.q.qsize()
        return res


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)