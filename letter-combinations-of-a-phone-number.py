class Solution(object):
    def letterCombinations(self, digits):

        if len(digits) == 0: return []

        m = {}

        m['2'] = ['a','b','c']
        m['3'] = ['d', 'e', 'f']
        m['4'] = ['g', 'h', 'i']
        m['5'] = ['j', 'k', 'l']
        m['6'] = ['m', 'n', 'o']
        m['7'] = ['p', 'q', 'r', 's']
        m['8'] = ['t', 'u', 'v']
        m['9'] = ['w', 'x', 'y', 'z']


        def help(digits, idx):

            if idx == len(digits):
                return [""]

            ar = m[digits[idx]]

            ans = help(digits, idx + 1)

            nans = []

            for i in range(len(ans)):
                for j in range(len(ar)):
                    nans.append(ar[j] + ans[i])

            return nans

        return help(digits, 0)
