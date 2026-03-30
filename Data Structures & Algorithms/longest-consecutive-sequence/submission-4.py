class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0 
        for x in seen:
            if x-1 not in seen:
                y = x
                length = 1
                longest = max(longest, length)
                while y + 1 in seen:
                    y += 1
                    length += 1
                    longest = max(longest, length)

        return longest