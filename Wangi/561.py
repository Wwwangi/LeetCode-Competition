#第一版答案
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(1,len(nums)+1):
            if(i%2==1):
                res+=nums[i-1]
        return res

#用切片，快速，但memory用的多
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res=sum(nums[::2])
        return res