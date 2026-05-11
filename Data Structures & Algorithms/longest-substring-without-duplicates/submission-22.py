class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = []
        left = 0 
        right = 0
        result = 0

        while right < len(s):
            while right < len(s) and s[right] in store:
                store.remove(s[left])
                left += 1
            store.append(s[right])
            right += 1
            result = max(result, right - left)
        return result