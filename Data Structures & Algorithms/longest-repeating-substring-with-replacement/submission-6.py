class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0
        freq = {}

        if len(s) == 0:
            return 0
        
        while right < len(s):
            window_size = right - left + 1
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1

            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
