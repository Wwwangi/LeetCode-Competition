class RecentCounter:

    def __init__(self):
        self.request=[]
        self.interval=3000

    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0]+3000<self.request[-1]:
            del self.request[0]
        return len(self.request)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)