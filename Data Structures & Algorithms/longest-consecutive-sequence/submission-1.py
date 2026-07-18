class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_ = set(nums)
        max_l = 0
        for val in hash_:
            l = 1
            while val + 1 in hash_:
                l += 1
                val = val + 1
            max_l = max(max_l, l)

        return max_l
        