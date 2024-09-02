# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def traverse(current):
            if current == None:
                return
            traverse(current.left)
            results.append(current.val)
            traverse(current.right)
        
        traverse(root)
        return results