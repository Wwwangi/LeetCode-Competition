#这个短的可以出来，长的超时了
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j] and j-i<=k):
                    return True
        return False

#特别慢，memory还高
import numpy as np
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index=np.argsort(nums)
        sort=np.sort(nums)
        for i in range(len(nums)-1):
            if(sort[i]==sort[i+1] and index[i+1]-index[i]<=k):
                return True
        return False

#hashtable
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable={}
        for i,v in enumerate(nums):
            if v in hashtable and i-hashtable[v]<=k:
                return True
            else:
                hashtable[v]=i
        return False