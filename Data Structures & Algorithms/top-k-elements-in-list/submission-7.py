class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            if num not in frq:
                frq[num] = 0
            else:
                frq[num] += 1
            result = sorted(frq, key=frq.get, reverse=True)
        return result[:k]