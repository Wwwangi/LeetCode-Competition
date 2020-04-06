class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        min=float('inf')
        for i in range(len(prices)):
            if(prices[i]<min):
                min=prices[i]
            elif(prices[i]-min>max):
                max=prices[i]-min
        return max