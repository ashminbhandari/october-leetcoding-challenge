class Solution(object):
    def minimumSwap(self, s1, s2):
        if len(s1) != len(s2): return -1
        m = {}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                st = str(s1[i]) + str(s2[i])
                if st not in m:
                    m[st] = 1
                else:
                    m[st] += 1
        n = 0
        if 'yx' in m:
            n += m['yx'] / 2
            m['yx'] = m['yx'] % 2
        if 'xy' in m:
            n += m['xy'] / 2
            m['xy'] = m['xy'] % 2
        if 'yx' in m and 'xy' in m and m['yx'] != m['xy']: return -1
        if 'yx' not in m and 'xy' in m and m['xy'] >= 1:
            return -1
        if 'xy' not in m and 'yx' in m and m['yx'] >= 1:
            return -1
        if 'yx' in m:
            n += m['yx']
        if 'xy' in m:
            n += m['xy']
        return n