class Solution(object):
    def productExceptSelf(self, nums):
        right_product = 1
        result = [1] * len(nums)

        for num in range(1, len(nums)):
            result[num] = result[num - 1] * nums[num-1]

        for num in range(len(nums)-2, -1, -1):
            right_product *= nums[num+1]
            result[num] *= right_product
            

        return result
        