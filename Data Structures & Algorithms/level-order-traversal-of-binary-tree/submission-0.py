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

        res = []
        current_level = 0
        current_res = []
        dq = deque([(root, 0)])
        while dq:
            node, level = dq.popleft()
            if level != current_level:
                res.append(current_res)
                current_res = []
                current_level = level

            current_res.append(node.val)    
            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))
        res.append(current_res)
        return res