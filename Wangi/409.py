class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        det=0
        res=0
        for char in s:
            dic[char]=dic.get(char,0)+1
        if(len(dic.keys())==1):
            return dic[s[0]]
        for key in dic.keys():
            if(dic[key]>=2 and dic[key]%2==0):
                res+=dic[key]
            elif(dic[key]>=2 and dic[key]%2==1):
                res+=dic[key]-1
                det=1
            else:
                det=1
        if(det==1):
            res+=1
        return res