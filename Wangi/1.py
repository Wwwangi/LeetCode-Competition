class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            other = target - nums[i]
            for j in range(i+1,len(nums)):
                if(nums[j]==other):
                    return [i,j]
                