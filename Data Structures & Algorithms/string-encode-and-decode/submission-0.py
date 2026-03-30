class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            # TODO: add length of s, then a special separator (like "#"), then the string itself
            # example: "neet" -> "4#neet"   
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # move j until you find '#'
            while s[j] != "#":
                j += 1
            length = int(s[i:j])               # number before '#'
            word = s[j+1 : j+1+length]         # substring of that length
            res.append(word)
            i = j + 1 + length                 # move to the next encoded word
        return res