#比较慢，第一版答案
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        i=0
        length=len(arr1)
        for item in arr2:
            while i<length:
                if(arr1[i]==item):
                    res.append(arr1[i])
                    del arr1[i]
                    i-=1
                    length-=1
                i+=1
            i=0
            print(arr1)
        arr1.sort()           
        for item in arr1:
            res.append(item)
        return res

#稍微快一些
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_unique_elements = sorted([x for x in arr1 if x not in arr2])
        new_list = []
        for num in arr2:
            new_list += [num] * arr1.count(num)
        return new_list + arr1_unique_elements

#非常精妙，temp.get(v,n): 找到temp的下标，如果没有，就是n，确保n比temp所有下标都大，然后对所有n的数，再比较v，这样后面unique的数字就会升序排列
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n=len(arr2)
        temp={v:k for k,v in enumerate(arr2)}
        res=sorted(arr1,key=lambda v: (temp.get(v,n),v))
        return res