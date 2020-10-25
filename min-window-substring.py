class Solution(object):
    def minWindow(self, s, t):

        sett = set(t)

        if len(t) > len(s): return ""

        lent = len(t)

        t = collections.Counter(t)

        if len(s) == lent and t != collections.Counter(s):
            return ""
        elif len(s) == lent and t == collections.Counter(s):
            return s

        start, end, minStart, minEnd, elems, found, foundCount = 0, 0, 0, sys.maxint, set(), {}, 0

        while end < len(s):

            if s[end] in t:

                if s[end] in found:

                    found[s[end]] += 1

                else:

                    found[s[end]] = 1

                if found[s[end]] == t[s[end]]:

                    foundCount += 1

            while start <= end and foundCount == len(t):

                if end - start < minEnd - minStart:
                    minEnd = end
                    minStart = start

                if s[start] in found:
                    found[s[start]] -= 1

                if s[start] in found and found[s[start]] < t[s[start]]:
                    foundCount -= 1

                start += 1

            end += 1

        return s[minStart:minEnd + 1] if minEnd != sys.maxint else ""




