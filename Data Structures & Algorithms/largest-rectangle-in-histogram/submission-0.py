class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                
                stackH, stackI = stack.pop()
                w = i - stackI
                area = w * stackH
                start = stackI
                maxarea = max(area, maxarea)
            
            stack.append([height,start])
        
        while stack:
            stackH, stackI = stack.pop()
            w = len(heights) - stackI
            area = w * stackH
            maxarea = max(area,maxarea) 

        return maxarea