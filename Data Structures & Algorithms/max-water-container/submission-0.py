class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        max = 0
        area = 0

        while l<r:
            if heights[l] < heights[r]:
                area = heights[l] * (r - l)
                l += 1
            
            elif heights[l] > heights[r]:
                area = heights[r] * (r - l)
                r -= 1
            elif heights[l] == heights[r]:
                area = heights[l] * (r - l)
                l += 1
            
            if area > max:
                    max = area
        print(l,r)
        return max

