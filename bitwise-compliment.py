class Solution(object):
    def bitwiseComplement(self, N):
        binaryRep = bin(N)
        mul = 0
        num = 0
        for i in range(len(binaryRep) - 1, 1, -1):
            tMul = 1
            if (binaryRep[i] == '1'):
                tMul = 0
            num = num + 2 ** mul * tMul
            mul += 1
        return num