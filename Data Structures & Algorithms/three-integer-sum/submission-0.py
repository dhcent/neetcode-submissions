class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 1):
            cur = nums[i]

            L = i + 1
            R = len(nums) - 1
            while L < R:
                total = nums[L] + nums[R]
                # they sum to 0
                if total == -cur:
                    triplets.add((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif total < -cur:
                    L += 1
                else:
                    R -= 1
                
        res = []
        for t in triplets:
            res.append(list(t))
        return res