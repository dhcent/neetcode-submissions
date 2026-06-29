import math

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # convert each letter in each word to ascii value. 
        # Separate characters by spaces, separate words by _
        # In decode, construct the letters by iterating through the entire new string.
        # iterate until you hit a space. Convert that ascii value to a character
        # Once you hit an underscore, append word to a list and then start on a 
        # new element in the list.

        # Here is correct approach:
        # isntead of using delimter, use a num followed by a # to separate words.
        # when we encode, put "len(word)#" and then the word. When decode, use number
        # to determine exactly when to splice.
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

