class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in dictionary:
                dictionary[key] = [word]
            else:
                dictionary[key].append(word)
        return list(dictionary.values())