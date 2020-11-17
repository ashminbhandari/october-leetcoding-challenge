class Solution(object):
    def countSquares(self, mat):
        cpx = [elem[:] for elem in mat]
        for i in range(len(cpx)):
            currOneCount = 0
            for j in range(len(cpx[0])):
                if cpx[i][j] == 1:
                    currOneCount += 1
                    cpx[i][j] = currOneCount
                else:
                    currOneCount = 0

        cpy = [elem[:] for elem in mat]
        for j in range(len(cpy[0])):
            currOneCount = 0
            column = []
            for i in range(len(cpy)):
                if cpy[i][j] == 1:
                    currOneCount += 1
                    cpy[i][j] = currOneCount
                else:
                    currOneCount = 0

        sq = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                pj = j
                for pi in range(i, len(mat)):
                    if pj >= len(mat[0]) or cpx[pi][pj] == 0: break
                    print cpx[pi][pj], cpy[pi][pj]
                    if cpy[pi][pj] >= (pi - i) + 1 and cpx[pi][pj] >= (pi - i) + 1: sq += 1
                    else: break
                    pj += 1

        return sq