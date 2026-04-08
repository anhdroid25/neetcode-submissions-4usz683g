class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            calculation = min(heights[left], heights[right]) * (right - left)
            if calculation > result:
                result = calculation
            elif heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -= 1
        return result