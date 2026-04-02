class Solution:
    delimiter = ";"

    def encode(self, strs: List[str]) -> str:
        total = ""
        for string in strs:
            total+=f"{len(string)}{self.delimiter}{string}"
        return total

    def decode(self, s: str) -> List[str]:
        output = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != self.delimiter:
                j += 1
            length = int(s[index:j])
            word = s[j + 1: j+ 1+length]
            output.append(word)
            index = j + 1 + length
        return output
