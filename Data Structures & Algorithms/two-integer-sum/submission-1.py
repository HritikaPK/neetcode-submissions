class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #brute-forcing
        # final = []
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             final.append(i)
        #             final.append(j)
        #             return(final)
        

        #hash-mapping
        map = {}
        final = []
        for i,value in enumerate(nums):
            map[value]=i
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res in map and map[res]!= i:
                final.append(i)
                final.append(map[res])
                return(final)
        return(final)

       





           


            
        