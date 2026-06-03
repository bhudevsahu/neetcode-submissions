# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def dfs(node, curLen):
            if not node:
                return

            curLen += 1
            self.maxD = max(self.maxD, curLen)
            dfs(node.left, curLen)
            dfs(node.right, curLen)

        dfs(root, 0)

        return self.maxD
