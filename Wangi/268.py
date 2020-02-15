#space达标，但速度很慢
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(nums==[0]):
            return 1
        elif(nums==[1]):
            return 0
        nums.sort()
        if(nums[0]==1):
            return 0
        for i in range(len(nums)-1):
            if(nums[i+1]-nums[i]!=1):
                return nums[i+1]-1
        return nums[-1]+1

#聪明的解法
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectedSum=n*(n+1)//2
        actualSum=sum(nums)
        return expectedSum-actualSum