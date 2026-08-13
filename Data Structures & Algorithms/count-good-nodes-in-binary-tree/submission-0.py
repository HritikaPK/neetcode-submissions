# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def findres(node, maxval):

            # null case
            if not node:
                return 0

            # if node is good or not
            if node.val >= maxval:
                res = 1
            else:
                res = 0
            
            maxval = max(maxval, node.val)
            
            res += findres(node.left, maxval)
            res += findres(node.right, maxval)

            return res
        return findres(root, root.val)
