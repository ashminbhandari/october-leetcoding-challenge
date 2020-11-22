class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        mx = 0
        while (i < j):
            mx = max(mx, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mx