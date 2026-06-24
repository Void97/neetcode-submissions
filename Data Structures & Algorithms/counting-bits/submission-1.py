class Solution:
    def countBits(self, n: int) -> List[int]:

        # ans = [0]*(n+1)
        # for i in range(n+1):
        #     count=0
        #     temp = i
        #     while temp > 0:
        #         count+=temp&1
        #         temp >>= 1
        #     ans[i] = count
        
        # return ans

        ans = [0]*(n+1)
        for i in range(1,n+1):
            ans[i] = ans[i>>1]+(i&1)
        return ans
        