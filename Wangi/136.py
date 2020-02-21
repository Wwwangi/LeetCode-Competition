class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for item in nums:
            if(item not in dic.keys()):
                dic[item]=1
            else:
                dic[item]+=1

        dic={v:k for k,v in dic.items()}
        for item in dic.keys():
            if(item==1):
                return dic[item]
                
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for item in nums:
            if(item not in dic.keys()):
                dic[item]=1
            else:
                dic[item]+=1

        dic={v:k for k,v in dic.items() if v==1}
        return dic[1]

#很机智
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)

#用XOR，太聪明了
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a^=i
        return a
                