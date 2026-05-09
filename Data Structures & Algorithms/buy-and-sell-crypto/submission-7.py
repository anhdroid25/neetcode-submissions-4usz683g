class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        highest = 0

        while right < len(prices):
            if prices[left] > prices[right]: #buying price is higher than selling price
                left = right
                right += 1
            else: #buying price is less than selling price
                result = prices[right] - prices[left]
                right += 1
                if result > highest:
                    highest = result
        return highest

