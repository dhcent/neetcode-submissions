class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        sol = []
        cur = 1

        zero_idx = None
        if nums[0] == 0:
            zero_idx = 0
        
        for i in range(1, len(nums)):
            if nums[i] == 0 and zero_idx == None:
                zero_idx = i
                cur *= nums[0]
            else:
                cur *= nums[i]

        if zero_idx != None:
            sol = [0] * len(nums)
            sol[zero_idx] = cur
            return sol
        
        sol.append(cur)
        
        for i in range(1, len(nums)):
            cur //= nums[i]
            cur *= nums[i - 1]
            sol.append(cur)
            print(cur)
        
        return sol

