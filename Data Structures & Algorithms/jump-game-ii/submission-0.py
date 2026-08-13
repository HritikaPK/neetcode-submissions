class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy instinct
        # how do i get to end with minimal jumps?

        # if we jump (1...x times) from x, how far does each position take us

        res = 0 # jumps in total 

        l = r = 0 #left  is 1 jump and right is x jumps 

        # if right == last index, we have arrived!

        while r < len(nums) - 1:

            far = 0 #farthest point (x jumps)

            for x in range(l,r+1):
                far = max(far, x + nums[x])
            
            l = r + 1
            r = far
            res += 1
        return res


