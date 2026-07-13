class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        def getNumCoins(curr_idx, rem_amt):
            if rem_amt == 0:
                return 0
            
            if curr_idx == n or rem_amt < 0:
                return float("inf")
            
            if memo[curr_idx][rem_amt] != -1:
                return memo[curr_idx][rem_amt]
            
            memo[curr_idx][rem_amt] = min(
                1 + getNumCoins(curr_idx, rem_amt - coins[curr_idx]),
                getNumCoins(curr_idx+1, rem_amt)
            )
            return memo[curr_idx][rem_amt]
        
        num_coins = getNumCoins(0, amount)
        return -1 if num_coins == float("inf") else num_coins