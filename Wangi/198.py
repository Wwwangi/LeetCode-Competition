class Solution:
    def rob(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        elif(len(nums)==1):
            return nums[0]
        elif(len(nums)==2):
            return max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            maxx=0
            for j in range(0,i-1):
                if(nums[j]>maxx):
                    maxx=nums[j]
            nums[i]+=maxx
        return max(nums[-1],nums[-2])

#初始化为0，可以从列表的第一项开始
class Solution:
    def rob(self, nums: List[int]) -> int:
        past=0
        now=0
        for num in nums:
            temp=now
            now=max(past+num,now)
            past=temp
        return now