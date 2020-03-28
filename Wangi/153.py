class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
     
#当rotated过后，list最左边的一定大于最右边的，当不再如此的时候，取最左边即为最小   
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            middle  = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        return nums[left]
        