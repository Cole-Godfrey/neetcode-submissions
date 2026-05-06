class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            encodedStr += str(len(string))
            encodedStr += "#"
            encodedStr += string
        print(encodedStr)
        return encodedStr
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            strs.append(s[i:j])
            i = j
        return strs

            