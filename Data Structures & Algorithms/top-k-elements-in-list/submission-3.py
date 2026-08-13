class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for c,v in count.items():
            freq[v].append(c)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        #########################################
        # # hashmap 
        # map = {}

        # # go through nums : [1 2 2 3 3 3]
        # for i in range(len(nums)):
        #     # nums[i] = 1
        #     # +1 for every instance of the number
        #     map[nums[i]] = 1 + map.get(nums[i],0) 
        #     # map[1] -> 1
       
        # map = dict(sorted(map.items(), key = lambda x: x[1]))
        # print(map)

        # return list(map.keys())[-k:]
        
        
        
       
        
        
        




        