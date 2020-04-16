class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        res=0
        count=0
        for char in s:
            if char in dic:
                res=max(res,count)
                for key in dic.keys():
                    if(dic[key]<dic[char]):
                        dic[key]=0
                    elif(key!=char and dic[key]>dic[char]):
                        dic[key]-=dic[char]
                count-=dic[char]
                count+=1
                dic[char]=count
            else:
                count+=1
                dic[char]=count
        res=max(res,count)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=[]
        res=0
        for char in s:
            if char in temp:
                res=max(res,len(temp))
                temp=temp[temp.index(char)+1:]
                temp.append(char)
            else:
                temp.append(char)
        res=max(res,len(temp))
        return res

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last, res, st = {}, 0, 0
        for i, v in enumerate(s):
            if v not in last or last[v] < st:
                res = max(res, i - st + 1)
            else:
                st = last[v] + 1
            last[v] = i
        return res