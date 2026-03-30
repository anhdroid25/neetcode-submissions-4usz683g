class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_result = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                result = prices[right] - prices[left]
                if result < max_result:
                    continue
                else:
                    max_result = result
        return max_result

