#可运行
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if(nums==[]):
            return []
        n=len(nums)
        temp=set([n for n in range(1,n+1)])
        nums=sorted(set(nums))
        result=temp.difference(nums)
        return result
        
#using hash table
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashtable=dict.fromkeys([n for n in range(1,len(nums)+1)], 0)
        for i in range(len(nums)):
            hashtable[nums[i]]=1
        return [k for k, v in hashtable.items() if v == 0]
            
#还有点问题
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if(nums==[]):
            return []
        n=len(nums)
        nums.sort()
        print(nums)
        result=[]
        pointer=1
        for i in range(n):
            if(nums[i]>pointer):
                result.append(pointer)
                pointer+=1
            elif(nums[i]==pointer):
                pointer+=1
        if(nums[-1]<=pointer):
            for i in range(nums[-1]+1,n+1):
                result.append(i)
        return result