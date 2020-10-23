class Solution(object):
    def find132pattern(self, nums):

        minUpto = [nums[0]] * len(nums)

        for i in range(1, len(nums)):

            minUpto[i] = min(minUpto[i - 1], nums[i])

        stack = []

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] > minUpto[i]:

                while len(stack) != 0 and stack[len(stack) - 1] <= minUpto[i]:
                    stack.pop(len(stack) - 1)

                if len(stack) != 0 and stack[len(stack) - 1] < nums[i]:
                    return True

                stack.append(nums[i])

        return False






