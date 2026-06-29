class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a num frequency hashmap
        # bucket sort hashmap by len of nums
        # iterate through bucket from the back to front until k elements are found.
        # T.C is O(n)
        num_freq = {}
        for num in nums:
            if num_freq.get(num, -1) == -1:
                num_freq[num] = 1
            else:
                num_freq[num] += 1

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

        for buck in reversed(bucket):
            if k <= 0:
                break
            if buck == None:
                continue
            for num in buck:
                res.append(num)
                k -= 1
                if k <= 0:
                    break
                

        return res


        



