class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set(nums1).intersection(set(nums2))
        return res

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        res=nums1&nums2
        return res