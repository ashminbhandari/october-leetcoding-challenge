class Solution(object):
    def minCost(self, s, cost):
        delCost = 0
        i = 0
        while i < len(s):
            cur = s[i]
            currCost = 0
            mx = -sys.maxint-1
            while i < len(s) and cur == s[i]:
                if cost[i] > mx:
                    mx = cost[i]
                currCost += cost[i]
                i += 1
            currCost -= mx
            delCost += currCost
        return delCost