class Solution:
    def findMin(self, nums: List[int]) -> int:  
        # Idea is to compare to left and right and have your left and right pointers ultimately "meet"
        # at the inflection point  
        # edge case for if it's already sorted.
        if nums[0] < nums[-1]:
            return nums[0]

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
        return nums[R]
