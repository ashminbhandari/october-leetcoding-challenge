class Solution(object):
    def removeDuplicateLetters(self, s):
        letters = {}
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else: letters[s[i]] = 1
        used = {}
        resultString = []
        for i in range(len(s)):
            letters[s[i]] -= 1
            if s[i] in used and used[s[i]] is True:
                continue
            while len(resultString) > 0 and s[i] < resultString[0] and letters[resultString[0]] > 0:
                used[resultString[0]] = False
                resultString.pop(0)
            resultString.append(s[i])
            used[s[i]] = True
        return "".join(resultString)