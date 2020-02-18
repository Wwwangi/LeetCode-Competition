#recursion
class Solution:
    def fib(self, N: int) -> int:
        if(N==0 or N==1):
            return N
        return self.fib(N-1)+self.fib(N-2)
     
#循环，效率更高    
class Solution:
    def fib(self, N: int) -> int:
        if(N==0 or N==1):
            return N
        elif(N==2):
            return 1
        res=1
        seq=[0,1]
        for i in range(2,N+1):
            res=seq[i-1]+seq[i-2]
            seq.append(seq[i-1]+seq[i-2])
        return res
            
#更快
class Solution:
    def fib(self, N: int) -> int:
        a,b=0,1
        for i in range(N):
        	a,b=a+b,a
        return a