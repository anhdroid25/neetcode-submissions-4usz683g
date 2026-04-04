class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                calculation = min(heights[i], heights[j]) * (j-i)
                result.append(calculation)
        return max(result)