class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right #always the result if there is no better

        while left <= right:
            mid_k = (left + right) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid_k)
            if h < hours:
                left = mid_k + 1
            else:
                right = mid_k - 1
                result = mid_k
        return result
