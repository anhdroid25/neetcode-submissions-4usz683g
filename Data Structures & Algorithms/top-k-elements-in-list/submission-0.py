class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # number -> frequency
        freq = [[] for i in range(len(nums) + 1)]  # buckets by frequency
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # count frequencies
        
        for n, c in count.items():
            freq[c].append(n)  # put number in its freq bucket
        
        res = []
        for i in range(len(freq) - 1, 0, -1):  # from high freq to low
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res  # return top k
