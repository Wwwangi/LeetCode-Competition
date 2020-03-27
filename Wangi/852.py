class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left=1
        right=len(A)-2
        while left<=right:
            temp=(left+right)//2
            print(temp)
            if A[temp-1]<A[temp]:
                left=temp+1
            else:
                right=temp-1
        return right

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        res=A.index(max(A))
        return res