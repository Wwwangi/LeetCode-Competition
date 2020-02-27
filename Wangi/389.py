class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic={}
        for char in s:
            dic[char]=dic.get(char,0)+1
        for char in t:
            dic[char]=dic.get(char,0)-1
        dic={k:v for v,k in dic.items()}
        res=dic[-1]
        return res