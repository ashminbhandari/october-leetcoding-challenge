class Solution(object):
    def maxProfit(self, k, prices):

        if len(prices) == 0 or k == 0:
            return 0

        if k >= len(prices) // 2:

            mx = 0

            for i in range(1, len(prices)):

                mx += max(prices[i] - prices[i - 1], 0)

            return mx

        #create dp array
        pdp = [0] * len(prices)

        dp = [0] * len(prices)

        for x in range(k):

            pdp = dp

            dp = [0] * len(prices)

            mx =  - sys.maxint - 1

            for i in range(1, len(dp)):

                mx = max(mx, - prices[i - 1] + pdp[i - 1])

                dp[i] = max(dp[i - 1], prices[i] + mx)


        return dp[-1]
