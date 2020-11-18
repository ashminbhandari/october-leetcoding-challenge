class Solution(object):
    def closeStrings(self, wa, wb):
        if len(wa) != len(wb): return False
        wma, fma, wmb, fmb = {}, {}, {}, {}
        for c in wa:
            if c in wma:
                if wma[c] in fma:
                    fma[wma[c]] -= 1
                wma[c] += 1
                if wma[c] in fma:
                    fma[wma[c]] += 1
                else:
                    fma[wma[c]] = 1
            else:
                wma[c] = 1
                if wma[c] in fma:
                    fma[wma[c]] += 1
                else:
                    fma[wma[c]] = 1
        for c in wb:
            if c in wmb:
                if wmb[c] in fmb:
                    fmb[wmb[c]] -= 1
                wmb[c] += 1
                if wmb[c] in fmb:
                    fmb[wmb[c]] += 1
                else:
                    fmb[wmb[c]] = 1
            else:
                wmb[c] = 1
                if wmb[c] in fmb:
                    fmb[wmb[c]] += 1
                else:
                    fmb[wmb[c]] = 1
        if fmb == fma and sorted(wmb.keys()) == sorted(wma.keys()): return True
        return False