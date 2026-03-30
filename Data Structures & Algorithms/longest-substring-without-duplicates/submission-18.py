class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = []
        result = 1
        left = 0
        
        if not s:
            return 0
        
        track.append(s[0])
        for right in range (1, len(s)):
            while s[right] in track:
                track.pop(0)
                left +=1
            track.append(s[right])
            
            if result < len(track):
                result = len(track)
        return result