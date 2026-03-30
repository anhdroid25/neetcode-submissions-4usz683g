class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_result = 0

        for right in range(1, len(prices)):
            result = prices[right] - prices[left]
            if prices[right] <= prices[left]:
                left = right
            else:
                if max_result < result:
                    max_result = result
        return max_result

        