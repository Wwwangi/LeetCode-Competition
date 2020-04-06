class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min=float('inf')
        for i in range(len(prices)-1):
            if(prices[i]<=min):
                min=prices[i]
            elif(prices[i+1]<prices[i]):
                profit+=prices[i]-min
                min=float('inf')
        if min!=float('inf') and prices[-1]>min:
            profit+=prices[-1]-min
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if(prices[i]>prices[i-1]):
                profit+=prices[i]-prices[i-1]
        return profit