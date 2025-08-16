class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[0]*(amount+1)
        for i in range(1,amount+1):
            minn=float('inf')
            for coin in coins:
                diff=i-coin
                if diff < 0:
                    break
                minn=min(minn,1+dp[diff])
            
            dp[i]=minn
        
        return dp[amount] if dp[amount] < float('inf') else -1
        