class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            if num not in frq:
                frq[num] = 0
            frq[num] += 1
        sort_freq = sorted(frq, key =lambda num: frq[num], reverse=True)
        return sort_freq[:k]



        