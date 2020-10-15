class Solution(object):
    def rotate(self, nums, k):
        if k == 0: return nums
        if len(nums) <= 1: return nums
        toMove = nums[0]
        i = k % len(nums)
        cnt = 0
        crcl = 0
        while cnt < len(nums):
            if i == crcl and cnt != 0:
                t = nums[i + 1]
                nums[i] = toMove
                toMove = t
                i += 1
                crcl = i
            else:
                t = nums[i]
                nums[i] = toMove
                toMove = t
            cnt += 1
            i = i + k
            i = i % len(nums)
        return nums