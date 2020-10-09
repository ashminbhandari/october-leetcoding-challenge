class Solution(object):
    def removeCoveredIntervals(self, intervals):
        if(len(intervals) == 0): return 0
        if(len(intervals) == 1): return 1
        intervals.sort()
        i = 0
        j = 1
        cnt = 0
        while (j < len(intervals)):
            if (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]):
                cnt += 1
                j += 1
            elif (intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]):
                cnt += 1
                i = j
                j += 1
            else:
                i = j
                j += 1
        return len(intervals) - cnt