class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # create adj list for each character
        adj = {c:set() for w in words for c in w}
        res = []
        # find nei to add to adj list
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]

            minlen = min(len(w1), len(w2))

            # check base case: invalid ordering
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # maintain a visit list: TRue: in current path - if seen True again = cycle 
        # visit - False once added to res: already processed
        visit = {}
        # dfs : post traversal : topological sort - adding children first
        def dfs(c):

            #base case: is c already in current path and to be yet added to res? -> cycle!!
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""

        res.reverse()

        return "".join(res)





        
