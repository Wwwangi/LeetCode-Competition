#用了sort的方法
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp=list(nums)
        temp.sort()
        print(temp)
        l=0
        r=0
        for i in range(len(nums)):
            if(nums[i]==temp[i]):
                l+=1
            else:
                break
        for j in range(len(nums)-1,-1,-1):
            if(nums[j]==temp[j]):
                r+=1
            else:
                break
        if(l+r>len(nums)):
            return 0
        return len(nums)-l-r