class TreeNode:
    def __init__(self):
        self.children = {}
        self.eOw = False

class PrefixTree:


    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.eOw = True


    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]

        if cur.eOw:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        return True
            
        
        