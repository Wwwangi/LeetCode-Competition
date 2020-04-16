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
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub not in dic:
                dic[nums[i]]=1
            else:
                return [nums.index(sub),i]
                