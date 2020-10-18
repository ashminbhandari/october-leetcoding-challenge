class Solution(object):
    def longestValidParentheses(self, s):
        o = []

        idxs = []

        for i in range(len(s)):

            if s[i] == "(":

                o.append(i)

            if s[i] == ")" and len(o) > 0:

                oi = o.pop()
                idxs.append(oi)
                idxs.append(i)

        idxs.sort()

        p = 1
        lp = 0

        for i in range (len(idxs) - 1):

            if idxs[i] + 1 == idxs[i + 1]:
                p += 1
                if p > lp:
                    lp = p
            else:
                if p > lp:
                    lp = p
                p = 1

        return lp






