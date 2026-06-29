import math

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            t = str(len(word)) + "#" + word
            res += t
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            # repeat looking for len until we hit a #
            word_len = 0
            while s[idx] != "#":
                word_len = word_len * 10 + int(s[idx])
                idx += 1
            idx += 1 #skip the #
            word = s[idx : idx + word_len] 
            res.append(word)
            idx += word_len
        return res

