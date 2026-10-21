class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp= [amount+1] * (amount+1)
        dp[0]=0 #base case

        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]= min(dp[a], 1+ dp[a-c])
                    # coin=4, amount=7
                    # dp[7]= min(dp[7], 1+ dp[7-4=3])
        return dp[amount] if dp[amount] != amount+1 else -1

        # O(amount* len(coins)) time
        # O(amount) space

        