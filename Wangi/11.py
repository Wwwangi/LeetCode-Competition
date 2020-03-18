#短的可出，长的超时
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                temp=min(height[i],height[j])*(j-i)
                if(temp>maxwater):
                    maxwater=temp
        return maxwater

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater=0
        left=0
        right=len(height)-1
        while(left<right):
            maxwater=max(maxwater,min(height[left],height[right])*(right-left))
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxwater