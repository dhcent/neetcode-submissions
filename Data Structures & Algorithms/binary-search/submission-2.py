class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        L = 0
        R = len(nums) - 1

        while L <= R:
            center = (L + R) // 2
            print(center)
            if nums[center] == target:
                return center
            elif nums[center] > target:
                R = center - 1
            else:
                L = center + 1
        return -1


        