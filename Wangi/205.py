class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp1=list(map(s.find,s))
        temp2=list(map(t.find,t))
        return temp1==temp2

#hashtable的版本
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        for i in range(len(s)):
            if(s[i] in dic.keys()):
                if(dic[s[i]]!=t[i]):
                    return False
            elif(t[i] in dic.values()):
                temp={v:k for k,v in dic.items()}
                if(temp[t[i]]!=s[i]):
                    return False
            else:
                dic[s[i]]=t[i]
        return True

#这个有一点问题，无法处理abab和abba这样的str
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp1={}
        temp2={}
        for char in s:
            temp1[char]=temp1.get(char,0)+1
        for char in t:
            temp2[char]=temp2.get(char,0)+1
        v1=list(temp1.values())
        v2=list(temp2.values())
        for i in range(len(v1)):
            if(v1[i]!=v2[i]):
                return False
        return True