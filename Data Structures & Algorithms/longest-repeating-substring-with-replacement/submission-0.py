class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a hashmap for the most frequently seen character
        # Create a sliding window with both L + R at 0
        # Shift R by 1 if Len - frequency_of_max < k (if the amount we need to replace < k)
        # Otherwise shift L by 1 and subtract from frequency as according
        # how to determine max?
        mp = {}
        seen = set()
        max_len = 0
        L, R = 0,0
        while R < len(s):
            if s[R] in seen:
                mp[s[R]] += 1
            else:
                mp[s[R]] = 1
                seen.add(s[R])
            cur_max = 0
            for freq in mp.values():
                cur_max = max(cur_max, freq)
            # it's not valid
            if (R - L + 1) - cur_max > k:
                mp[s[L]] -= 1
                L += 1
            
            max_len = max(max_len, R - L + 1)
            R += 1
        return max_len