#sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=0
        for i in range(k):
            res+=nums[i]
        i=k
        temp=res
        for i in range(k,len(nums)):
            temp+=nums[i]
            temp-=nums[i-k]
            res=max(temp,res)
        res=res/k
        return res

#超级快，beat99%，可是和上面有什么区别？ 可能是max用时较长
class Solution(object):
    def findMaxAverage(self, nums, k):
        m=a=sum(nums[:k])
        for i in range( len(nums) - k ):
            a += ( nums[k+i] - nums[i] )
            if a > m: m = a
        return m/float(k)

#看错题目了。。看成求一个subsequence让其average值最大了，实际上还有个k
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=len(nums)-1
        res=sum(nums[l:r+1])/(r-l+1)
        if(len(nums)==k):
            return res
        elif(k==1):
            return max(nums)
        det_l=0
        det_r=0
        count=0
        while(l<r):
            print(res)
            temp_l=sum(nums[l+1:r+1])/(r-l)
            if(temp_l>res):
                count+=1
                res=temp_l
                l+=1
            else:
                det_l=1
            if(l>=r or len(nums)-count==k):
                break
            temp_r=sum(nums[l:r])/(r-l)
            if(temp_r>res):
                count+=1
                res=temp_r
                r-=1
            else:
                det_r=1
            print(count)
            if(len(nums)-count==k):
                break
        return res