class Solution(object):
    def numSubmat(self, mat):

        og = [elem[:] for elem in mat]
        for i in range(len(mat)):
            currOneCount = 0
            row = []
            for j in range(len(mat[0]) - 1, -1, -1):
                if mat[i][j] == 1:
                    currOneCount += 1
                    mat[i][j] = currOneCount
                else:
                    currOneCount = 0

        rects = 0
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j] >= 1:
                    mi = sys.maxint
                    for x in range(i, len(mat)):
                        if mat[x][j] >= 1:
                            if mat[x][j] < mi:
                                mi = mat[x][j]
                            rects += mi
                        else: break

        return rects