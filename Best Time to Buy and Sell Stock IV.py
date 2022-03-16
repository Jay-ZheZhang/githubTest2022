class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # if k > len(prices) // 2:
            # return self.helper(prices)
        if len(prices) == 0: return 0
        dp = [[0] * (len(prices)) for i in range(k+1)]
        for i in range(1, k+1):
            maxAcc = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxAcc)
                maxAcc = max(maxAcc, -prices[j] + dp[i-1][j-1])
        return dp[-1][-1]
    def helper(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit