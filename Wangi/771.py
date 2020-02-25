class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic={}
        for char in S:
            dic[char]=dic.get(char,0)+1
        res=0
        for item in dic.keys():
            if(item in J):
                res+=dic[item]
        return res