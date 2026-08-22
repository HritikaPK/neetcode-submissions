class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0, 0
        maxLen = 0
        subset = set()

        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[r])
            w = (r-l)+1
            maxLen = max(maxLen,w)
        return maxLen
        