class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        sol = []

        for i in range(len(nums)):
            hmap[nums[i]] = hmap.get(nums[i],0) + 1

        sorted_items = sorted(hmap.items(), key=lambda kv: kv[1],reverse=True)
        print(sorted_items)

        while k:
            sol.append(sorted_items[k-1][0])
            k -= 1
        
        return sol
        
        
        




        