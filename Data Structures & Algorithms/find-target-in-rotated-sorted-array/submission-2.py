class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1]:
            R = 0
        else:
            L = 0
            R = len(nums) - 1
            # we want to terminate loop when they are adjacent to each other (at inflection point)
            while R - L > 1:
                center = int(L + (R - L) / 2)
                # left part of the list is sorted, inflection pt on right
                if nums[center] > nums[L]:
                    L = center
                else: #center < nums[L], inflection pt on the left
                    R = center
        print("R: ", R)
        #your shift is by R. so to determine 
        shift = R
        # implement binary search: L is 0, R is len - 1. When you access elements, add by shift
        # then mod the length
        L = 0
        R = len(nums) - 1
        while L <= R:
            center = L + (R - L) // 2
            val = nums[(center + shift) % len(nums)]
            print("val: ", val)
            print("L,R", L, R)
            if val == target:
                return (center + shift) % len(nums)
            elif val > target:
                R = center - 1
            else:
                L = center + 1
        return -1

