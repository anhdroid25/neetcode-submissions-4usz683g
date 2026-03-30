class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            area = min(heights[right], heights[left]) * (right - left) #always calculate the shorter one
            if area > result:
                result = area

            if heights[left] > heights[right]:
                right -= 1 #move shorter side because it is bottle neck
            elif heights[left] < heights[right]:
                left += 1
            elif heights[left] == heights[right]:
                left += 1
                right -= 1
        return result