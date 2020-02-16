#一开始想的，但是一个太慢的解法
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        temp=[]
        temp2=[]
        for string in queries:
            s=sorted(string)
            temp.append(s.count(s[0]))
        for string in words:
            w=sorted(string)
            temp2.append(w.count(w[0]))
        
        res=[]
        for i in range(len(temp)):
            summ=0
            for j in range(len(temp2)):
                if(temp[i]<temp2[j]):
                    summ+=1
            res.append(summ)
        
        return res

#二分插入法，把temp里的计数插入到temp2里
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        temp=[]
        temp2=[]
        for string in queries:
            s=min(string)
            temp.append(string.count(s))
        for string in words:
            w=min(string)
            temp2.append(string.count(w))
        res=[]
        temp2.sort()
        for i in range(len(temp)):
            x=len(temp2)-bisect.bisect(temp2,temp[i])
            res.append(x)
        return res

#更快的解答
import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            ss = min(s)
            return s.count(ss)
        
        q = [f(i) for i in queries]
        w = [f(i) for i in words]
        res = []
        w.sort()
        for index in range(len(q)):
            temp = len(w)-bisect.bisect(w, q[index])
            res.append(temp)
        return res