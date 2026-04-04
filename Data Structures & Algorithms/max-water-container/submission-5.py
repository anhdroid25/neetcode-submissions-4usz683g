class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            calculation = min(heights[left], heights[right]) * (right - left)
            result = max(calculation, result)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                right -=1
        return result