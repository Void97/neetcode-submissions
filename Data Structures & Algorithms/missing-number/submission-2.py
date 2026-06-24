class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n_xored = 0
        nums_xored = 0
        for i in range(len(nums) + 1):
            n_xored ^= i
        
        for num in nums:
            nums_xored ^= num
        
        return n_xored ^ nums_xored