import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones)>1):
            a=stones.pop()
            b=stones.pop()
            if(a==b):
                continue
            else:
                bisect.insort(stones,a-b)
        if(stones==[]):
            return 0
        else:
            return stones[0]