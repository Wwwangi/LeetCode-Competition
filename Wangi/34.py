class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        det=0
        while left<=right:
            temp=(left+right)//2
            if(nums[temp]<target):
                left=temp+1
            elif(nums[temp]>target):
                right=temp-1
            else:
                det=1
                start,end=temp,temp
                break
        if(det==0):
            return [-1,-1]
        temp2=temp
        while temp2<=len(nums)-1:
            if(nums[temp2]==target):
                end=temp2
            temp2+=1  
        while temp>=0:
            if(nums[temp]==target):
                start=temp
            temp-=1
        return [start,end]

#linear做法
class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

#二分
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        #determine the leftmost index
        while left<=right:
            temp=(left+right)//2
            if(nums[temp]<target):
                left=temp+1
            elif(nums[temp]>=target):
                right=temp-1
        leftmost=left
        left=leftmost
        right=len(nums)-1
        #determine the rightmost index
        while left<=right:
            temp=(left+right)//2
            if(nums[temp]<=target):
                left=temp+1
            elif(nums[temp]>target):
                right=temp-1
        rightmost=right
        if(leftmost>rightmost):
            return [-1,-1]
        return [leftmost,rightmost]

#整合版
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def index(left,right,direction):
            while left<=right:
                temp=(left+right)//2
                if(nums[temp]<target):
                    left=temp+1
                elif(nums[temp]>target):
                    right=temp-1
                else:
                    if(direction=='l'):
                        right=temp-1
                    else:
                        left=temp+1
            if(direction=='l'):
                return left   
            else:
                return right
            
        leftmost=index(0,len(nums)-1,'l')
        rightmost=index(leftmost,len(nums)-1,'r')
        if(leftmost>rightmost):
            return [-1,-1]
        return [leftmost,rightmost]