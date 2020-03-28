class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(matrix==[]):
            return False
        left=0
        right=len(matrix)*len(matrix[0])-1
        n=len(matrix[0])
        while left<=right:
            temp=(left+right)//2
            if(matrix[temp//n][temp%n]==target):
                return True
            elif(matrix[temp//n][temp%n]<target):
                left=temp+1
            else:
                right=temp-1
        return False