class Solution(object):
    def findMinArrowShots(self, points):
        if len(points) == 0: return 0
        points.sort()
        cnt = 0
        cr = points[0]
        i = 1
        while (i < len(points)):
            if max(cr[0], points[i][0]) <= min(cr[1], points[i][1]):
                cr = [max(cr[0], points[i][0]), min(cr[1], points[i][1])]
                cnt += 1
            else: cr = points[i]
            i += 1
        return len(points) - cnt