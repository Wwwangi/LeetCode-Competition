#time limit exceed
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res=[]
        for i in range(len(T)):
            count=0
            det=0
            for j in range(i+1,len(T)):
                if T[j]>T[i]:
                    count+=1
                    det=1
                    res.append(count)
                    break
                else:
                    count+=1
            if det==0 and j==len(T)-1:
                res.append(0)
        return res
                
#表现很差，5%，10%
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res=[]
        temp=[30000]*102
        for i in range(len(T)-1,-1,-1):
            day=min(temp[x] for x in range(T[i]+1,102))
            if(day<30000):
                res.insert(0,day-i)
            else:
                res.insert(0,0)
            temp[T[i]]=i
        return res
            
#把insert改成直接赋值，memory大幅提升
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res=[0]*len(T)
        temp=[30000]*102
        for i in range(len(T)-1,-1,-1):
            day=min(temp[x] for x in range(T[i]+1,102))
            if(day<30000):
                res[i]=day-i
            else:
                res[i]=0
            temp[T[i]]=i
        return res
            
#速度73%，用stack，需要加强理解！
class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans