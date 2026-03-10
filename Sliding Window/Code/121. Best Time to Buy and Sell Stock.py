'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxP

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         for i in range(len(prices)):
#             buy = prices[i]
#             for j in range(i + 1, len(prices)):
#                 sell  = prices[j]
#                 res = max(res, sell - buy)
#         return res

