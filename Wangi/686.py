#有点问题
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        res=1
        startPositionA,startPositionB=0,0
        for i in range(len(A)):
            if A[i]==B[0]:
                if(i==len(A)-1):
                    PositionA=0
                    res+=1
                else:
                    PositionA=i+1
                PositionB=1
                break
        if PositionB==0:
            return -1
        while PositionB<len(B):
            if A[PositionA]!=B[PositionB]:
                return -1
            else:
                if(PositionA==len(A)-1):
                    PositionA=0
                    res+=1
                else:
                    PositionA+=1
                PositionB+=1
        if(PositionA==0):
            res-=1
        return res
                
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        a = A
        count = 0
        while True:
            if B in a:
                return count + 1
            if len(A) * count > len(B):
                return -1
            a += A
            count += 1