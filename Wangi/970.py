class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res=[]
        i=0
        j=0
        while True:
            temp=x**i
            if(temp>bound):
                break
            while True:
                print(i,j)
                temp3=temp+y**j
                if(temp3 not in res):
                    if(temp3<=bound):
                        res.append(temp3)
                        j+=1
                    else:
                        j=0
                        break
                else:
                    j+=1
                if(y==1):
                    break
            i+=1
            if(x==1):
                break
        return res
                