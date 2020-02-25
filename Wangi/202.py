class Solution:
    def isHappy(self, n: int) -> bool:
        dic={}
        while(True):
            summ=0
            while(n>0):
                summ+=(n%10)**2
                n//=10
            if(summ==1):
                return True
            if(summ in dic.keys()):
                return False
            else:
                dic[summ]=1
                n=summ