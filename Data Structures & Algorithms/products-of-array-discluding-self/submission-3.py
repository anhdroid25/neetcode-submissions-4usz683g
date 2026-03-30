class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        result = []
        for num in range(1, len(nums)):
            left[num] = left[num - 1] * nums[num-1]
            
        for num1 in range(len(nums)-2, -1, -1):
            right[num1] = right[num1 + 1] * nums[num1 + 1]
        

        for num in range(len(nums)):
            result.append(left[num] * right[num])
        
        return result 
            
