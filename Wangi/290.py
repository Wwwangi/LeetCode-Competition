class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word=str.split(' ')
        dic={}
        if(len(pattern)!=len(word)):
            return False
        for i in range(len(word)):
            if(word[i] in dic.keys()):
                if(dic[word[i]]!=pattern[i]):
                    return False
            elif(pattern[i] in dic.values()):
                temp={k:v for v,k in dic.items()}
                if(temp[pattern[i]]!=word[i]):
                    return False
            else:
                dic[word[i]]=dic.get(word[i],pattern[i])
        return True

#map的做法，写起来比较简便
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p=list(map(pattern.find,pattern))
        t=str.split()
        s=list(map(t.index,t))
        return p==s