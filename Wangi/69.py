#大数字超时了
class Solution:
    def mySqrt(self, x: int) -> int:
        for num in range(0,x+1):
            if(num**2<=x and (num+1)**2>x):
                return num

#二分法
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = (right + left) // 2
            print(pivot)
            print(left,right)
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right