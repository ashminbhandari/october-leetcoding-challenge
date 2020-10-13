class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if sorted(A) != sorted(B): return False
        i = 0
        cnt = 0
        cntMap = {}
        while (i < len(A)):
            if A[i] in cntMap:
                cntMap[A[i]] = cntMap[A[i]] + 1
            else:
                cntMap[A[i]] = 1
            if (A[i] != B[i]):
                cnt += 1 
            if (cnt > 2):
                return False;
            i += 1
        if cnt == 2:
            return True
        if cnt == 0:
            for k in cntMap:
                if cntMap[k] >= 2: return True    
        return False