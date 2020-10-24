class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """

        tokens.sort()

        if len(tokens) == 0:
            return 0

        if P < tokens[0]:
            return 0

        if len(tokens) == 1 and P >= tokens[0]:
            return 1

        i = 0

        j = len(tokens) - 1

        S = 0

        maxS = 0

        while i <= j:

            if P < tokens[i] and S >= 1:

                P += tokens[j]
                S -= 1
                j -= 1

            else:

                while P >= tokens[i]:

                    S += 1
                    P -= tokens[i]
                    i += 1

                    if S > maxS:
                        maxS = S

        return maxS