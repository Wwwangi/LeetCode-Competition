#比较慢
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if(len(A)==1):
            return A
        l=0
        r=len(A)-1
        while(l<r):
            while(l<len(A)-1):
                if(A[l]%2==1):
                    break
                else:
                    l+=1
            while(r>0):
                if(A[r]%2==0):
                    break
                else:
                    r-=1
            if(l<r):
                A[l],A[r]=A[r],A[l]
                l+=1
                r-=1
        return A

#非常简便的做法
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans=sorted(A, key=lambda x: x%2)
        return ans
  
#第三种      
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res=[]
        for i in A:
            if(i%2==0):
                res.insert(0,i)
            else:
                res.append(i)
        return res
        