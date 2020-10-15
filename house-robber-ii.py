class Solution(object):
    def robOne(self, nums):
        p = 0
        n = 0
        
        for i in range(len(nums)):
            t = n
            n = max(nums[i] + p, n)
            p = t
        
        return n
    
    def rob(self, nums):        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
                    
        if len(nums) == 3:
            max(nums[0], nums[1], nums[2])
      
        return max(nums[0] + self.robOne(nums[2:len(nums) - 1]), self.robOne(nums[1:]))
       
        
      
        