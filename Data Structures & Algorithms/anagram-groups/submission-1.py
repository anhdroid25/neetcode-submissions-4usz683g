class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = {}

        for i in strs:
            key = tuple(sorted(i))
            if key in collect:
                collect[key].append(i)
            else:
                collect[key] = [i]
        return list(collect.values())
                