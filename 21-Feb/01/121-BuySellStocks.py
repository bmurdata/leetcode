# 2/1/21
# Find when to buy and sell stocks
# Question https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# My solution and Notes
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea- double pointer
        # Go from start to end and find the highest difference
        # Brute force, find all the sums, return the largest
        # Fails- memory limite excceed. complexity is O(n*2)
        # Other brute force- time limit exceeded
        # Solutions: Mine are one with O(n^2). However, one pass is better)
        minprice=99999
        maxprofit=0
        for price in prices:
            if price<minprice:
                minprice=dd
            elif price-minprice>maxprofit:
                maxprofit=price-minprice
        return maxprofit
        #largestDiff=0
        #for sellday in range(len(prices)-1):
         #   for buyday in range(sellday+1,len(prices)):
          #      
           #     if largestDiff< prices[buyday]-prices[sellday]:
            #        largestDiff=prices[buyday]-prices[sellday]
                
       # return largestDiff