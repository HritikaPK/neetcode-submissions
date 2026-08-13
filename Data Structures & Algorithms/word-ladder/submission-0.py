class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base case
        if endWord not in wordList:
            return 0

        # create a dict
        nei = collections.defaultdict(list)

        #populate dict using patterns and mapping them to the right words
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        # goes through each word - > finds pattern -> adds itself 

        visit = set([beginWord]) #to make sure we dont add the visited node to queue. We start with beginWord
        res = 1 # initially
        q = deque([beginWord]) # queue starts with begin word

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for j in range(len(curr)):
                    pattern = curr[:j] + "*" + curr[j+1:]
                    for neib in nei[pattern]:
                        if neib not in visit:
                            visit.add(neib)
                            q.append(neib)
            res += 1
        
        return 0


