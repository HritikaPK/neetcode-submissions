class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        # greedy logic: how do i check for optimal solution 

        # make sure no element in triplet is larger than values in target 
        # values in tagret should be maxs detected in the triplets

        zero = one = two = 0
        # traverse through each triplet O(n)

        for trip in triplets:
            # if any are greater than target, SKIP the triplet 
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            # check ai,bi,ci 

            if trip[0] == target[0]:
                zero = 1
            if trip[1] == target[1]:
                one = 1
            if trip[2] == target[2]:
                two = 1
        
        if zero == 1 and two == 1 and one == 1:
            return True
        else:
            return False
            # cehck if target values are present anywhere in the triplet. 
            # if all 3 target values have been spotted at the end, return TRUE
        