# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []

        # def traverse(node):
        #     if not node:
        #         return
        #     result.append(node.val)
        #     traverse(node.left)
        #     traverse(node.right)

        # traverse(root)
        # return result
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result
        
