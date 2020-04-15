#using division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        count=0
        res=[0 for n in range(len(nums))]
        for i in range(len(nums)):
            if(nums[i]==0):
                count+=1
                if(count==2):
                    return [0 for n in range(len(nums))]
                if(count==1):
                    position=i
            else:
                total*=nums[i]
        if(count==0):
            for i in range(len(nums)):
                res[i]=total//nums[i]
        elif(count==1):
            res[position]=total
        return res

#without division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1 for n in range(n)]
        right=[1 for n in range(n)]
        res=[0]*n
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        for i in range(n):
            res[i]=left[i]*right[i]
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        temp=1
        for i in range(1,n):
            res[i]=res[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            temp*=nums[i+1]
            res[i]*=temp
        return res
        
        