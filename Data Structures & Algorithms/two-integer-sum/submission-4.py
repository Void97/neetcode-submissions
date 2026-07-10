class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hasht = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hasht:
                return [hasht[diff], i]
            else:
                hasht[nums[i]] = i
