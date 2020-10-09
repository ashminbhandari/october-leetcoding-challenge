class Solution(object):
    def search(self, nums, target):
        def helpSearch(nums, target,start,end):
            if(end >= start):
                mid = (start + end) // 2
                if(target == nums[mid]): return mid
                elif (nums[mid] > target): return helpSearch(nums, target, start, mid - 1)
                else: return helpSearch(nums, target, mid + 1, end)
            else: return -1
        return helpSearch(nums, target,0,len(nums) - 1)

