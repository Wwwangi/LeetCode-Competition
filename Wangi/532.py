class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        res=0
        if(k<0):
            return 0
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        if(k==0):
            for key in d.keys():
                if(d[key]>=2):
                    res+=1
        else:
            for key in d.keys():
                if(key+k in d.keys()):
                    res+=1
        return res

#大神的做法，可以写成一行
class Solution:
    def findPairs(self, nums, k):
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0