class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # bucket
        freq = [[] for i in range(len(nums)+1)]

        #hmap to store counts initially 
        counter = defaultdict()

        for i in nums:
            counter[i] = 1 + counter.get(i,0)

        for q,v in counter.items():
            freq[v].append(q)
        
        res = []

        for a in range(len(freq)-1,0,-1):
            for n in freq[a]:
                if len(res) < k:
                    res.append(n)
        return res

