class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for x in seen:
            if x-1 not in seen:
                length = 1
                while x + length in seen:
                    length += 1
                longest = max(longest, length)

        return longest