# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def check(node):
            if node == None:
                return 0
            left, right = check(node.left), check(node.right)
            if abs(right - left) > 1:
                self.balance = False
            return max(left, right) + 1
        check(root)
        return self.balance