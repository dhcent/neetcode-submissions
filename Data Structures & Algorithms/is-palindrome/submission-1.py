class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (s.lower()).replace(" ", "")
        temp = ""
        for char in s:
            if ord(char) >= 97 and ord(char) <= 122 or char.isnumeric():
                temp += char

        s = temp
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True