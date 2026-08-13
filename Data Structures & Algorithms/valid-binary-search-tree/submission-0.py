# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def value(node, left, right):
            
            #Case 1: empty tree = BST
            if not node:
                return True 
            
            #check limits on left and right for node
            if not left < node.val < right:
                return False
            
            return (value(node.left, left, node.val) and value(node.right, node.val, right))

            
        
        return value(root, float('-inf'), float('inf'))
            