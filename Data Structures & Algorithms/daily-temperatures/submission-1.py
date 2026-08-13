class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[temp,indx]

        for i,v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                stTemp, stIdx = stack.pop()
                res[stIdx] = i - stIdx
            
            stack.append([v,i])
        return res
        



        