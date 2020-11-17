class Solution(object):
    def isAlienSorted(self, words, order):
        m = {}
        for i in range(len(order)):
            m[order[i]] = i
        for i in range(1, len(words)):
            j = 0
            while j < len(words[i]) and j < len(words[i - 1]) and words[i - 1][j] == words[i][j]:
                j += 1
                if j >= len(words[i]) and j < len(words[i - 1]):
                    return False
            if j < len(words[i - 1]) and j < len(words[i]) and m[words[i - 1][j]] > m[words[i][j]]:
                return False
        return True