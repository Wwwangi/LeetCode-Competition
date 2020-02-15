class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=list(set(nums))
        diff=len(nums)-len(temp)
        if(diff!=0):
            return True
        else:
            return False