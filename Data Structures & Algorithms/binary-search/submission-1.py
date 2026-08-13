class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums)-1

        # [1 2 3 4 5 6 7 8]
        #  L             R

        while l<=r:

            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1        