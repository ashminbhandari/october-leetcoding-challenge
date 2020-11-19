class Solution(object):
    def coinChange(self, coins, amt):
        self.m = {}
        def help(coins, amount):
            if amount in self.m:
                return self.m[amount]
            if amount == 0:
                return 0 #0 ways to make 0 coin
            if amount < 0:
                return sys.maxint
            minWays = sys.maxint
            for i in range(len(coins)):
                ways = help(coins, amount - coins[i]) + 1
                if ways < minWays:
                    minWays = ways
            self.m[amount] = minWays
            return minWays
        ans = help(coins, amt)
        return ans if ans != sys.maxint else -1