class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums=list(set(nums))
        left=0
        right=len(nums)-1
        while left<=right:
            temp=(left+right)//2
            if(nums[temp]==target):
                return True
            elif(nums[temp]>=nums[left]):
                if(target>=nums[left] and target<nums[temp]):
                    right=temp-1
                else:
                    left=temp+1
            else:
                if(target<nums[left] and target>nums[temp]):
                    left=temp+1
                else:
                    right=temp-1
                
        return False


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            temp=(left+right)//2
            if(nums[temp]==target):
                return True
            while left<temp and nums[left]==nums[temp]:
                left+=1
            if(nums[temp]>=nums[left]):
                if(target>=nums[left] and target<nums[temp]):
                    right=temp-1
                else:
                    left=temp+1
            else:
                if(target<nums[left] and target>nums[temp]):
                    left=temp+1
                else:
                    right=temp-1
                
        return False