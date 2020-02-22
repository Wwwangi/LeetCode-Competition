#我的写法
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={}
        for char in text:
            dic[char]=dic.get(char,0)+1
        dic={k:v for k,v in dic.items() if (k in 'balloon')}
        if(len(dic.keys())==5):
            dic['l']//=2
            dic['o']//=2
            res=min(dic.values())
            return res
        else:
            return 0

#fromkeys的用法
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic=dict.fromkeys('balloon',0)
        for char in text:
            if(char in 'balloon'):
                dic[char]+=1
        dic['l']//=2
        dic['o']//=2
        res=min(dic.values())
        return res