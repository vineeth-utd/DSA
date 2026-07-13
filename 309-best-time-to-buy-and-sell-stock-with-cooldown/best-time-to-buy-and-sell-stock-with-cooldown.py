# Bottom up tabulation
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         dp = [[0] * 2 for _ in range(n+2)]
        
#         for curr_idx in range(n-1, -1, -1):
#             for can_buy in [0, 1]:



# Top down memoization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1] * 2 for _ in range(n+2)]

        def getMaxProfit(curr_idx, can_buy):
            if curr_idx >= n:
                return 0
            
            if memo[curr_idx][can_buy] != -1:
                return memo[curr_idx][can_buy]
            
            skip_profit = getMaxProfit(curr_idx + 1, can_buy)

            action_profit = 0

            if can_buy:
                action_profit = getMaxProfit(curr_idx + 1, 0) - prices[curr_idx]
            else:
                action_profit = getMaxProfit(curr_idx + 2, 1) + prices[curr_idx]

            memo[curr_idx][can_buy] = max(skip_profit, action_profit)
            return memo[curr_idx][can_buy]
        
        return getMaxProfit(0, 1)