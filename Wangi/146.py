class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.usage={}
        self.capacity=capacity
        self.state=1

    def get(self, key: int) -> int:
        if(key in self.cache.keys()):
            self.usage[key]=self.state
            self.state+=1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys() and len(self.cache.keys())==self.capacity:
            temp=min(self.usage.values())
            tempkey={v:k for k,v in self.usage.items() if v==temp}
            deletekey=tempkey[temp]
            del self.cache[deletekey]
            del self.usage[deletekey]   
        self.cache[key]=value
        self.usage[key]=self.state
        self.state+=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#用python排序字典做的
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)