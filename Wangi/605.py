class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(len(flowerbed)==1):
            if(flowerbed[0]==0 and n<=1):
                return True
            elif(flowerbed[0]==1 and n==0):
                return True
            else:
                return False
        
        if(flowerbed[0]==0 and flowerbed[1]==0):
            n-=1
            flowerbed[0]=1
        if(flowerbed[-1]==0 and flowerbed[-2]==0):
            n-=1
            flowerbed[-1]=1
        for i in range(1,len(flowerbed)-1):
            if(flowerbed[i]==1):
                continue
            else:
                if(flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    if(n==0):
                        break
                    n-=1
                    flowerbed[i]=1
        print(n)
        if(n>0):
            return False
        else:
            return True

#往array前后各加个0
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        i = 0
        flowerbed.append(0)
        flowerbed.insert(0,0)
        while i < len(flowerbed)-2:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] ==0:
                cnt += 1
                i += 2
            else:
                i += 1
        if cnt < n:
            return False
        else:
            return True