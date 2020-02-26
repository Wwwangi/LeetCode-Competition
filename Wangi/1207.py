class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for num in arr:
            dic[num]=dic.get(num,0)+1
        used=[]
        for num in dic.values():
            if(num not in used):
                used.append(num)
            else:
                return False
        return True

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for num in arr:
            dic[num]=dic.get(num,0)+1
        a=len(dic.values())
        b=len(set(dic.values()))
        return a==b