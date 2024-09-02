# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        def check(node, targetSum):
            if node.left == None and node.right == None:
                return targetSum - node.val == 0
            
            left = check(node.left, targetSum - node.val) if node.left else False
            right = check(node.right, targetSum - node.val) if node.right else False

            return left or right
        
        return check(root, targetSum)