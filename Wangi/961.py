class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        size=len(A)/2
        dic={}
        for num in A:
            dic[num]=dic.get(num,0)+1
            if(dic[num]==size):
                return num

#排序法
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        n=len(A)//2
        if(A[n-1]==A[n-2]):
            return A[n-1]
        return A[len(A)//2]

#
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        appeared=[]
        for num in A:
            if num not in appeared:
                appeared.append(num)
            else:
                return num

#random法，意外的可能很快
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        while(True):
            temp=random.sample(A,2)
            if(temp[0]==temp[1]):
                return temp[0]