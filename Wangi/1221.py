class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0
        l=0
        res=0
        for char in s:
            if(char=='R'):
                r+=1
            else:
                l+=1
            if(r==l):
                res+=1
        return res