class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        tracker = 0
        longest = 0

        for num in nums:
            seen.add(num)
        
        for num in seen:
            start = 0
            if num - 1 not in seen:
                start = num
                current_longest = 1
                while (start + 1) in seen:
                    start += 1
                    current_longest += 1
                
                if current_longest > longest:
                    longest = current_longest
        
        return longest


