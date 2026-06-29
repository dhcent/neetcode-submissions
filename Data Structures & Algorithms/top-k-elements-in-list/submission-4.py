class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a num frequency hashmap
        # bucket sort hashmap by len of nums
        # iterate through bucket from the back to front until k elements are found.
        # T.C is O(n)
        num_freq = {}
        for n in nums:
            num_freq[n] = num_freq.get(n,0)+1

        bucket = [None] * len(nums)

        # iterate through each num and freq in num_freq dict. 
        for num, freq in num_freq.items():
            # note indexes in bucket refer to frequency, thus must decrement
            idx = freq - 1
            if bucket[idx] == None:
                bucket[idx] = [num]
            else:
                bucket[idx].append(num)

        res = []
        idx = len(nums) - 1

        while k > 0 and idx >= 0:
            if bucket[idx]:
                res.append(bucket[idx].pop())
                k-=1
            else:
                idx -= 1

        return res


        



