class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += (str(len(word)) + "#" + word)
        return encode

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            length = s[i:j]
            result = s[j+1 : j + 1 + int(length)]
            decoded.append(result)
            i = j + 1 + int(length)
        return decoded