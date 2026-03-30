class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if num - 1 not in seen:
                current_longest = 1
                while (num + 1) in seen:
                    num +=1
                    current_longest += 1
                longest = max(current_longest, longest)
        return longest


