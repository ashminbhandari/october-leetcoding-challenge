class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        i = 0
        j = 0
        while i <= nums[len(nums) - 1]:
            if len(nums) - j == i:
                return i
            while(j < len(nums) and nums[j] == i):
                j += 1
            i += 1
            if i > len(nums) - j:
                break
        return -1
