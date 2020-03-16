#单个可出，太长超时
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        def addeven(B):
            summ=0
            for num in B:
                if num%2==0:
                    summ+=num
            return summ
        
        res=[]
        for query in queries:
            index=query[1]
            addNum=query[0]
            A[index]+=addNum
            summ=addeven(A)
            res.append(summ)
        return res

#ac
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        S=sum(x for x in A if x%2==0)
        res=[]
        for addNum, index in queries:
            if(A[index]%2==0):
                S-=A[index]
            A[index]+=addNum
            if(A[index]%2==0):
                S+=A[index]
            res.append(S)
        return res