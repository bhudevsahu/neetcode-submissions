# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        
        def dfs(node):
            if not node:
                return -1

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            curHeight = max(leftHeight, rightHeight) + 1

            if curHeight == len(self.res):
                self.res.append([])

            self.res[curHeight].append(node.val)
            return curHeight

        dfs(root)

        return self.res