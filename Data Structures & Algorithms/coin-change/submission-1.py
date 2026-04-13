from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array. We use float('inf') to represent unreachable amounts.
        # We need array size to be amount + 1 to store answers for 0 through 'amount'.
        
        dp = [float('inf')] * (amount + 1)
        
        # Base case: It takes 0 coins to make the amount 0
        dp[0] = 0
        
        # Work our way up iteratively from amount 1 to the target amount
        for a in range(1, amount + 1):
            for coin in coins:
                # If we can use this coin (the current amount is at least the coin's value)
                if a - coin >= 0:
                    # The minimum coins needed is either what we already have for this amount,
                    # or 1 (the current coin) + the minimum coins needed for the remainder.
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                    
        # If the target amount is still infinity, we couldn't find a combination
        return dp[amount] if dp[amount] != float('inf') else -1