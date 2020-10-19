class Solution(object):
    def minDominoRotations(self, A, B):

        if A == B:
            return 0

        el = A[0]

        aCnt = 0

        for i in range(len(A)):

            if A[i] != el:
                if B[i] != el:
                    aCnt = sys.maxint
                    break
                aCnt += 1

        el = B[0]

        bCnt = 0

        for i in range(len(A)):

            if A[i] != el:
                if B[i] != el:
                    bCnt = sys.maxint
                    break
                bCnt += 1

        el = A[0]

        cCnt = 0

        for i in range(len(B)):

            if B[i] != el:
                if A[i] != el:
                    cCnt = sys.maxint
                    break
                cCnt += 1

        el = B[0]

        dCnt = 0

        for i in range(len(B)):

            if B[i] != el:
                if A[i] != el:
                    dCnt = sys.maxint
                    break
                dCnt += 1

        r = min(aCnt, bCnt, cCnt, dCnt)

        return r if r != sys.maxint else -1