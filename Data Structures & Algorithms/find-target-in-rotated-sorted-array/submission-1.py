class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <=r:

            #find m

            m = (l + r) // 2

            if nums[m] == target:
                return m

            #left sorted array
            if nums[l] <= nums[m]:

                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1 
            
            #right sorted array
            if nums[r] >= nums[m]:

                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1 

        return -1

        