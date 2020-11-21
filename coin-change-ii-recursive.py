class Solution(object):
    def change(self, amount, coins):
        self.m = {}
        def help(amount, coins, i):
            k = str(amount) + ',' + ',' + str(i)
            if k in self.m:
                return self.m[k]
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0
            ways = 0
            ways += help(amount - coins[i], coins, i) + help(amount, coins, i + 1)
            self.m[k] = ways
            return ways
        return help(amount,coins, 0)