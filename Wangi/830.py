class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        start=0
        count=1
        res=[]
        for i in range(len(S)-1):
            if(count==1):
                position=i
            if(S[i+1]==S[i]):
                count+=1
            if(S[i+1]!=S[i] or i==len(S)-2):
                if(count>=3):
                    res.append([position,position+count-1])
                    count=1
                else:
                    count=1
        return res

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        c1=''
        start=0
        res=[]
        for i, c2 in enumerate(S+'.'):
            if(c1!=c2):
                if(i-start>=3):
                    res.append([start,i-1])
                start=i
            c1=c2
        return res