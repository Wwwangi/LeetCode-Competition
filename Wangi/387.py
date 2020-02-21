class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for char in s:
            dic[char]=dic.get(char,0)+1
        for item in dic.keys():
            if(dic[item]==1):
                res=s.index(item)
                return res
        return -1