class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = []
        stack = []

        for i in range(len(position)):
            pair.append([position[i],speed[i]])

        pair.sort(key = lambda x:x[0], reverse = True)

        # print(pair)

        for p,s in pair:

            d = target - p
            t = d/s
            if not stack:
                stack.append(t)

            if stack and t > stack[-1]:
                stack.append(t)
            
        
        return len(stack)
            # print(p)
            # print(s)