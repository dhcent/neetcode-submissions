class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [0] * len(nums)
        suf = [0] * len(nums)
        prefix_prod = 1
        suffix_prod = 1
        for i in range(len(nums)):
            pref[i] = prefix_prod
            suf[len(nums) - 1 - i] = suffix_prod
            prefix_prod *= nums[i]
            suffix_prod *= nums[len(nums) - 1 - i]

        return [a * b for a, b in zip(pref, suf)]
            
        


