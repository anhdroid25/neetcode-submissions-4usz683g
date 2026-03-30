class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_length = 1 #always 1 when it is empty
        char = []

        if not s: #if s is emtpy
            return 0

        char.append(s[0])
        for right in range(1, len(s)):
            while s[right] in char:
                char.pop(0)
                left += 1
            char.append(s[right])
            if max_length < len(char):
                max_length = len(char)
        return max_length