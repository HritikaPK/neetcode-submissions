class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        solution = []

        for i in range(len(strs)):
            
            sorted_i = "".join(sorted(strs[i]))
            if sorted_i in hmap:
                hmap[sorted_i].append(strs[i])
            else:
                hmap[sorted_i] = [strs[i]]
        
        return list(hmap.values())
        
        
        
    

