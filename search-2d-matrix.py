class Solution(object):
    def searchMatrix(self, matrix, target):

        if len(matrix) == 0 or len(matrix[0]) == 0: return False

        w = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][w] >= target:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                return False

        return False