class Solution:
    def titleToNumber(self, s: str) -> int:
        ans=0
        count=0
        for i in range(len(s)-1,-1,-1):
            ans+=26**count*(ord(s[i])-64)
            count+=1
        return ans