class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums: #loop through the whole thing to keep count
            if num not in frq: #initialize the number when not in dict
                frq[num] = 0 #new key so initialize count to 0
            frq[num] += 1 # always increment the count if seen
        sort_freq = sorted(frq, key=frq.get, reverse=True)
# sorted(iterable, key=None, reverse=False/True)-> returns a new sorted list
# frq          -> iterates over the dictionary keys (the numbers)
# key=frq.get  -> sort by each key's frequency value
# reverse=True -> largest frequency first because you want top k
# sort_freq    -> stores the sorted list
        
        #list[start:stop:step]
        return sort_freq[:k] #slice from index 0 up to k (since python grabs from 0)



        