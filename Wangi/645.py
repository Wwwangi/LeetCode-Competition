class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dic={}
        res=[]
        for i in range(1,n+1):
            dic[i]=0
        for num in nums:
            dic[num]+=1
            if(dic[num]==2):
                res.append(num)
        miss={v:k for k,v in dic.items() if v==0}
        res.append(miss[0])
        return res