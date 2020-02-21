#可以说是medium了
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        det=False
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                if det:
                    return False
                if(i>=2 and nums[i]<nums[i-2]):
                    nums[i]=nums[i-1]
                det=True
        return True