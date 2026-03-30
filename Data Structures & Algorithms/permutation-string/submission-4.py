class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0] * 26, [0] * 26 
        matches = 0
        left = 0
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index_right = ord(s2[right]) - ord('a')
            s2Count[index_right] += 1
            if s1Count[index_right] == s2Count[index_right]:
                matches += 1
            elif s1Count[index_right] + 1 == s2Count[index_right]:
                matches -= 1

            index_left = ord(s2[left]) - ord('a')
            s2Count[index_left] -= 1
            if s1Count[index_left] == s2Count[index_left]:
                matches += 1
            elif s1Count[index_left] - 1 == s2Count[index_left]:
                matches -= 1
            
            left += 1
        return matches == 26