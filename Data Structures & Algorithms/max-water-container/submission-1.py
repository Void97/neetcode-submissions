class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            area = max(area,width*min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        
        return area
