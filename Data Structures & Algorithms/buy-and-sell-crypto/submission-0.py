class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, buy = 0,0
        localProfit, globalProfit = 0,0
        if len(prices) == 1:
            return 0
        for i in range(len(prices)):
            buy = prices[i]
            l = i+1
            while l < len(prices):
                sell = prices[l]
                localProfit = sell - buy
                if localProfit <= 0:
                    l +=1
                    continue
                elif localProfit > globalProfit:
                    globalProfit = localProfit
                    l +=1
                else:
                    l +=1
        return globalProfit