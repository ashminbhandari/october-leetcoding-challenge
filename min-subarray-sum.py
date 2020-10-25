class Solution(object):
    def minSubArrayLen(self, s, nums):
        twosideq = []
        xsum = 0
        l = sys.maxint
        for i in range(len(nums)):
            xsum += nums[i]
            twosideq.append(nums[i])
            while xsum >= s and len(twosideq) != 0:
                if len(twosideq) < l:
                    l = len(twosideq)
                xsum -= twosideq.pop(0)
        return l if l != sys.maxint else 0