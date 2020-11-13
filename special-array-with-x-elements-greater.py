class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        i = 0 #range 0 to max (numx)
        j = 0 #array iterator idx
        while i <= nums[len(nums) - 1]: #go through entire range
            if len(nums) - j == i: #if there are exactly i elements remaining from current idx in the sorted array
                return i
            while(j < len(nums) and nums[j] == i): #if in the array we reach a value representation of i, increase j
                j += 1
            i += 1
            if i > len(nums) - j: #if the i we have is more than the elements remain, break out
                break
        return -1
