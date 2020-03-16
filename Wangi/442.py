class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                res.append(nums[i])
        return res

#用了hash table，但是memory用很多
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp={}
        res=[]
        for num in nums:
            temp[num]=temp.get(num,0)+1
        for key in temp.keys():
            if(temp[key]==2):
                res.append(key)
        return res

#超时了
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        temp=len(nums)
        for i in range(1,n+1):
            j=0
            while j < temp:
                if(nums[j]==i):
                    del nums[j]
                    temp-=1
                    break
                j+=1
        return nums

#很smart的想法
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for num in nums:
            if(nums[abs(num)-1]<0):
                res.append(abs(num))
            else:
                nums[abs(num)-1]*=-1
        return res