#两循环，都很垃圾
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers=[n for n in numbers if n < target]
        temp=[]
        for i in range(len(numbers)):
            if(numbers[i] not in temp):
                temp.append(numbers[i])
            else:
                continue
            for j in range(len(numbers)-1,i,-1):
                if(numbers[i]+numbers[j]==target):
                    return [i+1,j+1]
                elif(numbers[i]+numbers[j]<target):
                    break

#双指针，很快很牛逼
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers=[n for n in numbers if n < target]
        i=0
        j=len(numbers)-1
        while(i<j):
            if(numbers[i]+numbers[j]==target):
                return [i+1,j+1]
            elif(numbers[i]+numbers[j]>target):
                j-=1
            else:
                i+=1
        