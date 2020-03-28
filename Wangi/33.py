#确定target是在单调递增那一侧的子串上还是在shift之后那一侧的子串上，然后再决定往左右哪一侧移动
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            temp=(left+right)//2
            print(temp)
            if(nums[temp]==target):
                return temp
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
                
        return -1