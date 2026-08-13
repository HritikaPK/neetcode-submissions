class TreeNode:

    def __init__(self):
        self.children = {}
        self.eOw = False
    
    def AddWord(self,word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.eOw = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode()

        for w in words:
            root.AddWord(w)

        rows = len(board)
        columns = len(board[0])

        res, visit = set(), set()

        def dfs(r,c,node,word):

            if (r < 0 or c < 0 or r == rows or c == columns or board[r][c] not in node.children or (r,c) in visit):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.eOw == True:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))

        for r in range(rows):
            for c in range(columns):
                dfs(r,c,root,"")
        
        return list(res)
        