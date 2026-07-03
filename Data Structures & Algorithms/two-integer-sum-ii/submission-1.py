class Solution:
    # haven't we done this bruh
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 1
        R = len(numbers)
        # when accessing have to minus one to involve 1-indexed indices
        while L < R:
            total = numbers[L - 1] + numbers[R - 1]
            if total == target:
                return [L, R]
            if total < target:
                L += 1
            else:
                R -= 1
        