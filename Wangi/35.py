class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums[0]>target):
            return 0
        elif(nums[-1]<target):
            return len(nums)
        for i in range(len(nums)):
            if(nums[i]==target or (nums[i]>target)):
                result=i
                break
        return result

#改良版
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums[0]>target):
            return 0
        elif(nums[-1]<target):
            return len(nums)
        for i in range(0,len(nums)):
            if(nums[i]>=target):
                return i