class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        gls = []
        ngls = 1
        for i in range(100):
            gls.append([0] * ngls)
            ngls += 1
        gls[0][0] = poured
        for i in range(1, 100):
            for j in range(len(gls[i]) - 1):
                q = (gls[i - 1][j] - 1) / 2.0
                if q > 0:
                    gls[i][j] += q
                    gls[i][j + 1] = q
        return min(1, gls[query_row][query_glass])