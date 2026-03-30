class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums: #loop through the whole thing to keep count
            if num not in frq: #initialize the number when not in dict
                frq[num] = 0
            frq[num] += 1 # always increment the count if seen
        #frq is the dictionary
        # frq[num] is the value
        sort_freq = sorted(frq, key=lambda num: frq[num], reverse=True)
#           |      |    |   |          |            |
#           |      |    |   |          |            sort largest to smallest
#           |      |    |   |          look up the frequency of each key
#           |      |    |   placeholder variable for each key
#           |      |    sort by this value
#           |      the dictionary keys (the numbers)
#           store the sorted list
        
        return sort_freq[:k]



        