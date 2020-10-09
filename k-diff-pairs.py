class Solution(object):
    def findPairs(self, nums, k):
        if (len(nums) <= 1): return 0
        nums.sort()
        i = 0
        j = 1
        cnt = 0
        pa = None
        pb = None
        while (i != j and j < len(nums)):
            if(nums[j] - nums[i] == k):
                if (nums[j] != pb and nums[i] != pa): cnt += 1
                pb = nums[j]
                pa = nums[i]
                i += 1
                j += 1
            elif(nums[j] - nums[i] < k):
                j += 1
            elif(nums[j] - nums[i] > k):
                i += 1
                if (i == j): j += 1
        return cnt