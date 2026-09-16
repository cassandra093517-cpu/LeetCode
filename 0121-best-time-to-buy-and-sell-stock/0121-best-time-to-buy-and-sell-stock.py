class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i,j=0,0
        profit=0
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
            profit=max(profit, (prices[j]-prices[i]))
            j+=1
        return profit


        


        

        