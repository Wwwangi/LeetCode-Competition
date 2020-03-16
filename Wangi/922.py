class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res=[0 for x in range(len(A))]
        position_even=0
        position_odd=1
        for num in A:
            if(num%2==0):
                res[position_even]=num
                position_even+=2
            else:
                res[position_odd]=num
                position_odd+=2
        return res