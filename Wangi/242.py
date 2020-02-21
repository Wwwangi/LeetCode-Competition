class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if(s==t):
            return True
        else:
            return False

#用了hash table，速度memory都有很大提升
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        if(s=='' and t==''):
            return True
        for char in s:
            dic[char]=dic.get(char,0)+1
        for char in t:
            dic[char]=dic.get(char,0)-1
        for i in dic.values():
            if(i!=0):
                return False
        return True