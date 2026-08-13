# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # set current to the root

        curr = root

        #loop through to search the tree
        while curr:

            # if p and q are greater than curr
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if p and q are less than curr 
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # if p and q split 
            # curr is one of the p or q nodes
            else:
                return curr
