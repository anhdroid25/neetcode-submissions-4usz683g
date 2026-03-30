class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequency = {}
        result = 0

        for right in range(len(s)):
            window_size = right - left + 1
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            if window_size - max(frequency.values()) > k:
                frequency[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result



            