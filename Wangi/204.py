#超时
class Solution:
    def countPrimes(self, n: int) -> int:
        res=0
        for num in range(2,n):
            det=0
            for factor in range(2,num):
                if(num%factor==0):
                    det=1
            if(det==0):
                res+=1
        return res

class Solution:
    def countPrimes(self, n: int) -> int:
        p = [1]*n
        res = 0
        for i in range(2,n):
            if p[i]: 
                res+=1
                j = 2
                while j*i<n:
                    p[i*j] = 0
                    j+=1
        return res

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<2):
            return 0
        prime = [1]*n
        prime[0],prime[1]=0,0
        for i in range(2,int(n**0.5)+1):
            if prime[i]: 
                j = 2
                while j*i<n:
                    prime[i*j] = 0
                    j+=1
        return sum(prime)