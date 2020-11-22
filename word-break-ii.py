class Solution(object):
    def wordBreak(self, s, wordDict):
        self.m = {}
        def wordBreaker(s):
            if s in self.m:
                return self.m[s]
            if not s:
                return [""]
            ans = []
            for word in wordDict:
                if word == s[:len(word)]:
                    res = wordBreaker(s[len(word):])
                    for r in res:
                        if len(r) == 0: ans.append(word)
                        else: ans.append(word + " " + r)
            self.m[s] = ans
            return ans
        return wordBreaker(s)