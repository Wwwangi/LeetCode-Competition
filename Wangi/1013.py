class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total=sum(A)
        if(total%3!=0):
            return False
        else:
            splitsum=total//3
            print(splitsum)
            leftsum=A[0]
            rightsum=A[-1]
            i=0
            j=len(A)-1
            while(i+1<j):
                if(leftsum==splitsum and leftsum==rightsum):
                    return True
                if(leftsum!=splitsum):
                    i+=1
                    leftsum+=A[i]
                if(rightsum!=splitsum):
                    j-=1
                    rightsum+=A[j]
            return False

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:        
        sumA,s,c = sum(A),0,0
        if sumA % 3 == 0:             
            while A and c<2:
                s += A.pop()
                if s*3 == sumA:
                    c += 1
                    s = 0
        return c == 2 and A and sum(A)*3==sumA