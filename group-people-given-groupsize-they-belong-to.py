class Solution(object):
    def groupThePeople(self, groupSizes):
        m = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in m:
                m[groupSizes[i]] = [i]
            else:
                m[groupSizes[i]].append(i)

        ans = []
        for k in m.keys():
            arr = m[k]
            i = 0
            while i < len(arr):
                ans.append(arr[i:i+k])
                i += k
        return ans