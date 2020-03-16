#超时
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        res=0
        for i in range(len(A)-1):
            first=A[i]
            second=A[i+1]
            for j in range(i+2,len(A)):
                if(A[j]<first+second and first+second+A[j]>res):
                    res=first+second+A[j]
        return res

#因为要求最大，倒着省时                   
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        res=0
        for i in range(len(A)-1,-1,-1):
            first=A[i]
            second=A[i-1]
            for j in range(i-2,-1,-1):
                if(first<second+A[j] and first+second+A[j]>res):
                    return first+second+A[j]
                elif(first>second+A[j]):
                    break
        return 0
                    
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        res=0
        i=len(A)-1
        while i >= 2:
            first=A[i]
            second=A[i-1]
            third=A[i-2]
            if(first<second+third):
                    return first+second+third
            i-=1
        return 0
                    