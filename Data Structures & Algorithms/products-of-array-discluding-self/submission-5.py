class Solution(object):
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        right = 1

        for num in range(1, len(nums)):
            left[num]  = left[num-1] * nums[num-1]
        
        for num in range(len(nums)-2, -1, -1):
            right *= nums[num+1]
            left[num] *= right
        
        return(left)