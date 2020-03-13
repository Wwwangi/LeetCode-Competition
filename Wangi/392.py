class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current=0
        i=0
        while i<len(t):
            if(current==len(s)):
                break
            if(t[i]==s[current]):
                current+=1
                i+=1
            else:
                i+=1
        if(current==len(s)):
            return True
        else:
            return False
                
class Solution:
    def isSubsequence(self, s, t):
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True

#如果找不到就会返回1
class Solution:
    def isSubsequence(self, s, t):
        det=-1
        for c in s:
            det=t.find(c,det+1)
            if(det==-1):
                return False
        return True