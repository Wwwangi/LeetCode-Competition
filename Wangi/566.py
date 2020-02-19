#用了numpy函数，但速度贼慢
import numpy as np
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp=np.array(nums)
        temp=temp.flatten()
        if(temp.shape[0]==r*c):
            res=np.reshape(nums,(r,c))
            return res
        else:
            return nums

#暴力法，速度超过42，memory超越100
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if(len(nums)*len(nums[0])==r*c):
            temp=[]
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    temp.append(nums[i][j])
            res=[]
            element=[]
            count=0
            for i in range(len(temp)):
                element.append(temp[i])
                count+=1
                if(count==c):
                    res.append(element)
                    count=0
                    element=[]
            return res
        else:
            return nums

#和暴力法异曲同工之妙，但是写的更加聪慧
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        for i in nums:
            temp += i
        if len(temp) == r * c:
            res = []
            for i in range(0, len(temp),c):
                res.append(temp[i: i + c])
            return res
        return nums