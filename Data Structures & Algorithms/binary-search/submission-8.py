class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            equation = (left + right) // 2
            if nums[equation] == target:
                return equation
            elif nums[equation] < target:
                left = equation + 1
            elif nums[equation] > target:
                right = equation - 1
        return -1

