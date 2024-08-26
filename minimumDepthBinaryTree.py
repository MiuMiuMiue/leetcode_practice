# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.minHeight = 2 ** 30

        def height(node, depth):
            if node.left == None and node.right == None:
                self.minHeight = min(self.minHeight, depth + 1)
                return
            if node.left:
                height(node.left, depth + 1)
            if node.right:
                height(node.right, depth + 1)
        
        height(root, 0)
        return self.minHeight
        
