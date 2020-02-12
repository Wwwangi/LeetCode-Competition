class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        while(i<len(nums)):
            if(nums[i]==nums[i-1]):
                nums.pop(i)
                i-=1
            i+=1
        return len(nums)