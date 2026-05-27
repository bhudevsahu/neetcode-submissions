# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            res = self.isSameTree(node, subRoot)
            if node is None:
                return False
            if not res:
                return dfs(node.left) or dfs(node.right)
            return res

        return dfs(root)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False