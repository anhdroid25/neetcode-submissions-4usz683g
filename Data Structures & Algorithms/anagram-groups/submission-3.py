class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {} #immutable and can be hashed

        for words in strs:
            key = tuple(sorted(words)) #has to be immutable to be a key
            if key not in diction:
                diction[key] = [words]
            else:
                diction[key].append(words)
        return list(diction.values())

