class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # create a hashmap showing last indexes
        lastindex = {}
        maxi = 0
        sub = []
        size = 0

        for i,v in enumerate(s):
            lastindex[v] = i
        
        # traverse through s
        for i,v in enumerate(s):
            maxi = max(maxi,lastindex[v])
            size += 1
            if i == maxi:
                sub.append(size)
                size = 0
        return sub




        

