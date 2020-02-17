#负数有问题
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=[abs(n) for n in nums]
        nums.sort()
        return nums[-1]*nums[-2]*nums[-3]

#有些用例通不过
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        product=1
        l=0
        r=len(nums)-1
        while(l<=r and count<3):
            count+=1
            print(product)
            if(abs(nums[l])>abs(nums[r])):
                product*=nums[l]
                l+=1
            else:
                product*=nums[r]
                r-=1                   
        return product

#ok
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res=max(nums[-3]*nums[-2]*nums[-1],nums[0]*nums[1]*nums[-1])
        return res