class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        longest = 0 

        for n in nums:
            # check: if its a starter
            if n-1 not in hashset:
                length = 0
                while length+n in hashset:
                    length += 1
                longest = max(longest,length)

        return longest