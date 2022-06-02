class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window with two pointers        
        l,r = 0,1 # l = buy and r = sell 
        maxP = 0
        
        while(r < len(prices)):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # buy the dip
            r += 1
            
            
        return maxP