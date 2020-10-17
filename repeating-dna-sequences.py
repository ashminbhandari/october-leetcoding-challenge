class Solution(object):
    def findRepeatedDnaSequences(self, s):

        if len(s) <= 10: return []

        ss = s[:10]

        m = set()

        m.add(ss)

        i = 10

        ans = set()

        while i < len(s):

            ss = ss[1:10] + s[i]

            if ss in m:
                ans.add(ss)
            else:
                m.add(ss)
            i += 1

        return list(ans)