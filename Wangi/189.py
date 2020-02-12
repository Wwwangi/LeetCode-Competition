#整个list翻转，再分别翻转两部分
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        def reverse(a,start,end):
            while(start<end):
                a[start],a[end]=a[end],a[start]
                start+=1
                end-=1
        k=k%len(nums)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)

#append比insert占用内存多，但速度快
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for i in range(len(nums)-k):
            nums.append(nums[0])
            del nums[0]