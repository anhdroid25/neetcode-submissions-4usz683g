class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left= 0 
        right = 1
        highest = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                result = prices[right] - prices[left]
                right += 1
                if result > highest:
                    highest = result
        return highest
 