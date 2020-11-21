class Solution(object):
    def coinChange(self, coins, amt):
        dp = [[0] * (len(coins) + 1)]
        row = [0] * (len(coins) + 1)
        for i in range(amt):
            row[0] = sys.maxint
            dp.append(row[:])
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i][j - 1]
                if i - coins[j - 1] >= 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - coins[j - 1]][j] + 1)
        return dp[-1][-1] if dp[-1][-1] != sys.maxint else -1