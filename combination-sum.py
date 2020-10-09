class Solution(object):
    def combinationSum(self, candidates, target):
        self.combs = []

        def helpMe(candidates, target, c, k):
            if (target == 0):
                self.combs.append(c[:])
                return

            if (target < 0):
                return

            for i in range(k, len(candidates)):
                c.append(candidates[i])
                helpMe(candidates, target - candidates[i], c, i)
                c.pop()

        helpMe(candidates, target, [], 0)

        return self.combs