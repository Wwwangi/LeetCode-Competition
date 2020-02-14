#use hashtable
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable={}
        for i in range(len(nums)):
            if(nums[i] in hashtable.keys()):
                hashtable[nums[i]]+=1
            else:
                hashtable[nums[i]]=1
        
        result=[k for k,v in hashtable.items() if v>(len(nums)/2)]
        return result[0]

#排序，排在中间的那个数一定是多数元素
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums[int(len(nums)/2)]

#标答，很快
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        return max(count.keys(),key=count.get)