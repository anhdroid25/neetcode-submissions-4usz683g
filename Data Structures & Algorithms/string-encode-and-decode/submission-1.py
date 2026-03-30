class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in range(len(strs)):
            encode += str(len(strs[i])) + "#" + strs[i]
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_words = []     
        while i < len(s):
            j = s.index("#", i)
            length = s[i:j]
            result = s[j+1 : j + 1 + int(length)]
            decoded_words.append(result)
            i = j + 1 + int(length)
        return decoded_words

