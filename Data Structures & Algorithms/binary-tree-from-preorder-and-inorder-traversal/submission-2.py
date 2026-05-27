# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {v: i for i, v in enumerate(inorder)}
        self.index = 0

        def dfs(l, r):
            if l > r:
                return None

            rootVal = preorder[self.index]
            self.index += 1
            rootIndex = inMap[rootVal]
            root = TreeNode(rootVal)
            root.left = dfs(l, rootIndex - 1)
            root.right = dfs(rootIndex + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)