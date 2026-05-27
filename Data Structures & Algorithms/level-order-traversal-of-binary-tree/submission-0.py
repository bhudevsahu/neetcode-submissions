# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        output: List[List[int]] = []
        while len(queue) > 0:
            level_values = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_values.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            output.append(level_values)
        
        return output
                
        