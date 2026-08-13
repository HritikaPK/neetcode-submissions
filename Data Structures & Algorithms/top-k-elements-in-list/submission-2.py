class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap 
        map = {}

        # go through nums : [1 2 2 3 3 3]
        for i in range(len(nums)):
            # nums[i] = 1
            # +1 for every instance of the number
            map[nums[i]] = 1 + map.get(nums[i],0) 
            # map[1] -> 1
       
        map = dict(sorted(map.items(), key = lambda x: x[1]))
        print(map)

        return list(map.keys())[-k:]
        
        
        
       
        
        
        




        