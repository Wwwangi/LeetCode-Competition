class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if(len(nums)<=1):
            return [str(x) for x in nums]
        det=True
        for i in range(len(nums)-1):
            if det:
                start=nums[i]
                end=nums[i]
                det=False
            if(nums[i+1]==nums[i]+1):
                end=nums[i+1]
            else:
                det=True
            if(i+1==len(nums)-1 and end==nums[-1]):
                det=True
            if det:
                if(start==end):
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
            if(i+1==len(nums)-1 and end!=nums[-1]):
                res.append(str(nums[-1]))         
        return res