# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #dfs

        if not root:
            return 0
        
        count = 0
        
        stack = [(root,root.val)]

        while stack:
            
            node,MaxSoFar = stack.pop()

            if node.val >= MaxSoFar:
                count += 1
            newmax = max(MaxSoFar, node.val)
            if node.right: 
                stack.append((node.right,newmax))
                
            if node.left: 
                stack.append((node.left,newmax))         

        return count
                

            

          


        

        