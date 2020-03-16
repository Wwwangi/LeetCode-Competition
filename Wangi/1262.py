class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0]*3
        for num in nums:
            for i in dp[:]:
                dp[(num+i)%3]=max(dp[(num+i)%3],num+i)
        return dp[0]

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
            3  6  5  1   8  
        0   3  9  9  15  18 
        1   0  0  0  10  10 
        2   0  0  14 0   23
        
            1  2  3  4  4
        0   0  3  6  9  12
        1   1  1  4 10  13
        2   0  2  5  8  14
        
        '''
        
        m = [[0 for n in range(len(nums))] for n in range(3)]
        m[nums[0] % 3][0] = nums[0]
        
        for i in range(1, len(nums)):
            for j in range(3):
                m[j][i] = m [j][i-1]
        
            for j in range(3):
                n = m[j][i-1] + nums[i]
                mod = n % 3
                if m[mod][i] < n:
                    m[mod][i] = n
                    
        
        return m[0][-1]