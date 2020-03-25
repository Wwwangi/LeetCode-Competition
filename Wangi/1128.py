#超时了
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res=0
        def compare(pair1,pair2):
            if(pair1[0]==pair2[0] and pair1[1]==pair2[1]):
                return True
            if(pair1[0]==pair2[1] and pair1[1]==pair2[0]):
                return True
            return False
        for i in range(len(dominoes)-1):
            for j in range(i+1,len(dominoes)):
                if(compare(dominoes[i],dominoes[j])):
                    res+=1
        return res

#用hashmap，dictionary的key不能用list，只能用tuple
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res=0
        temp={}
        for domino in dominoes:
            if((domino[0],domino[1]) not in temp.keys()):
                if((domino[1],domino[0]) not in temp.keys()):
                    temp[(domino[1],domino[0])]=1
                else:
                    res+=temp[(domino[1],domino[0])]
                    temp[(domino[1],domino[0])]+=1
            else:
                res+=temp[(domino[0],domino[1])]
                temp[(domino[0],domino[1])]+=1
        return res

#降维，很机智，两个一位数可以变成一个两位数
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res=0
        temp=[0]*100
        for domino in dominoes:
            n=min(domino[0],domino[1])*10+max(domino[0],domino[1])
            temp[n]+=1
        for i in temp:
            if(i>1):
                res+=i*(i-1)//2
        return res