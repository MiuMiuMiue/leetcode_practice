# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if (left == None and right != None) or (left != None and right == None):
                return False
            elif left == None and right == None:
                return True
            
            if not self.isSameTree(left.left, right.right):
                return False
            if left.val != right.val:
                return False
            if not self.isSameTree(left.right, right.left):
                return False
            
            return True
        
        return check(root.left, root.right)