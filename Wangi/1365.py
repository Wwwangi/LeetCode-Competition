class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=[0]*101
        res=[]
        for num in nums:
            temp[num]+=1
        for num in nums:
            res.append(sum(temp[:num]))
        return res

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp={}
        nums2=sorted(nums)
        res=[]
        for i,num in enumerate(nums2):
            if(i>0 and nums2[i-1]==num):
                temp[num]=temp[nums2[i-1]]
            else:
                temp[num]=i
        for num in nums:
            res.append(temp[num])
        return res