class Solution(object):
    def trap(self, height):
        if not height: return 0
        seen = set()
        cur = 0
        mcur = 0
        cm = height[0]
        cmi = 0
        for i in range(1, len(height)):
            if height[i] <= cm:
                cur += cm - height[i]
            else:
                seen.add(str(cmi) + "," + str(i))
                mcur += cur
                cm = height[i]
                cmi = i
                cur = 0
        cur = 0
        cm = height[-1]
        cmi = len(height) - 1
        for i in range(len(height) - 2, -1, -1):
            if height[i] < cm:
                cur += cm - height[i]
            elif str(i) + "," + str(cmi) not in seen:
                mcur += cur
                cm = height[i]
                cur = 0
                cmi = i
        return mcur
