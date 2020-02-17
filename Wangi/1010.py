#超时了
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res=0
        for i in range(len(time)):
            for j in range(i+1,len(time)):
                if((time[i]+time[j])%60==0):
                    res+=1
        return res

#not optimal
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res=0
        remainder=[0]*60
        for i in range(len(time)):
            res+=remainder[(60-time[i])%60]
            remainder[time[i]%60]+=1
        return res

#很快，但memory低
class Solution:
    def numPairsDivisibleBy60(self, T: List[int]) -> int:
        freq, res = [0] * 60, 0
        for t in T:  # count the freq
            freq[t % 60] += 1
        for i in range(31):  # check "0 - 30" (i-th)
            if (i == 0 or i == 30):  # e.g: 60, 180, 360, 720
                n = freq[i]
                res += n * (n - 1) // 2  # combination (pick two of them up)
            else:
                res += freq[i] * freq[60 - i]  # permutation
        return res

#非常快
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        r=0
        t=[0]*60
        for i in time:
            t[i%60]+=1
        r=r+int(t[0]*(t[0]-1)/2)+int(t[30]*(t[30]-1)/2)
        for j in range(1,30):
            r+=t[j]*t[60-j]
        return r