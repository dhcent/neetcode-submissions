class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:\

    # Iterate through nums
    # Create a hashmap that maps num to max group len.
    # set val equal to mp[# - 1] + mp[# + 1] + 1 (conjoining two contiguous sets) .get(# +- 1, 0)
    # If we update the value, we must update edge values as well (bubble to edges)
    # Keep a tracker of max len. If new len greater than max len, update max len. 
        res = 0
        seen = set()
        mp = {}
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            size = mp.get(num - 1, 0) + mp.get(num + 1, 0) + 1
            # update size if larger than current max
            res = max(res, size)
            mp[num] = size
            if mp[num] > 1: #mp has joined a group, therefore must update the bounds of the group
                L = num - 1
                R = num + 1

                # Find edges and update edge map values to new larger size
                while L in seen:
                    L -= 1
                while R in seen:
                    R += 1
                mp[L + 1] = size
                mp[R - 1] = size
        
        return res



