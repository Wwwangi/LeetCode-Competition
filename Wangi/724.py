#第一版答案，cumulative法，速度超越81，memory超越100，用了太多判定...
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if(nums==[]):
            return -1
        temp=[]
        cul=0
        for item in nums:
            cul+=item
            temp.append(cul)
        det=False
        if(sum(nums[1:len(nums)])==0):
            return 0
        for i in range(len(temp)-1):
            if(temp[i]==temp[-1]-temp[i+1]):
                res=i+1
                det=True
                break

        if(det==True):
            return res
        elif(sum(nums[0:len(nums)-1])==0):
            return len(nums)-1
        else:
            return -1

#意思差不多的解法，但不知为何速度比较慢
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        temp=0
        for i in range(len(nums)):
            if(total-temp-nums[i]==temp):
                return i
            temp+=nums[i]
        return -1