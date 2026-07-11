class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use the bucket sort
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        freqs = [[] for _ in range(len(nums) + 1)]
        for n, count in d.items():
            freqs[count].append(n)
        
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        