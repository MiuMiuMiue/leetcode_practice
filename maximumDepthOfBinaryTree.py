# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def check(current, depth):
            if not current:
                return depth
            left = check(current.left, depth + 1)
            right = check(current.right, depth + 1)
            return max(left, right)
        
        return check(root, 0)