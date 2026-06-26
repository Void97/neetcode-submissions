class Solution:
    def reverse(self, x: int) -> int:
        
        res = list(str(abs(x)))

        l = 0
        r = len(res) - 1
        while l < r:
            res[l], res[r] = res[r], res[l]

            l += 1
            r -= 1
        
        res = ''.join(res)
        # if int(res) >= -2**31 and int(res) <= 2**31-1:
        if int(res) in range(-2**31,2**31):
            return int(res) if x > 0 else -int(res)
        else:
            return 0