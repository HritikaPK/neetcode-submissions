class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        # heapify nums
        heapq.heapify(nums)
        print(nums)
        # pop elements till size = k ex k = 2,1
        while len(nums) > k:
            heapq.heappop(nums)
            
        print(nums)
        return nums[0]


        # return last elemnt