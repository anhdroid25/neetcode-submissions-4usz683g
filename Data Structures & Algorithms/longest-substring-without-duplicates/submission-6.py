class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_length = 1
        char = []

        if not s:
            return 0

        char.append(s[0])
        for right in range(1, len(s)):
            if s[right] not in char:
                pass
            else:
                while s[right] in char:
                    char.pop(0)
                    left += 1
            char.append(s[right])
            if max_length < len(char):
                max_length = len(char)
        return max_length