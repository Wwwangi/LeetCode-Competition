class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        totalType=len(set(candies))
        if(totalType>=len(candies)//2):
            return len(candies)//2
        else:
            return totalType

#速度超过94，memory超过100
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        ans=min(len(candies)//2,len(set(candies)))
        return ans