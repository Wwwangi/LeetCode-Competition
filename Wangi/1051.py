class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp=sorted(heights)
        res=0
        for i in range(len(heights)):
            if(heights[i]!=temp[i]):
                res+=1
        return res
                