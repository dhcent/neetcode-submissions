class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 1
        L = 0
        R = 1
        seen = set()
        seen.add(s[L])
        while R < len(s):
            if s[R] not in seen:
                seen.add(s[R])
                R += 1
            else: 
                max_len = max(max_len, len(seen))
                # need to move left pointer up, removing elements from seen as necessary
                while s[L] != s[R]:
                    seen.remove(s[L])
                    L += 1
                L += 1 # move left pointer to one idx right
                R += 1

        return max(max_len, len(seen))
