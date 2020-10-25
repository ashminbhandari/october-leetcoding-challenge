class Solution(object):
    def smallestRange(self, A):
        pq = [(row[0], idx, 0) for idx, row in enumerate(A)]
        heapq.heapify(pq)
        right = max(row[0] for row in pq)
        mxleft, mxright = 0, sys.maxint
        while heapq:
            left, i, j = heapq.heappop(pq)
            if right - left < mxright - mxleft:
                mxright = right
                mxleft = left
            if j + 1 < len(A[i]):
                heapq.heappush(pq, (A[i][j + 1], i, j + 1))
                if A[i][j + 1] > right: right = A[i][j + 1]
            else:
                return mxright, mxleft