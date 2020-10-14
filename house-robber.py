class Solution(object):
    def rob(self, nums):

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        p = nums[0]
        n = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            t = n
            n = max(nums[i] + p, n)
            p = t

        return n
