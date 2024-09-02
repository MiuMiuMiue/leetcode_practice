# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check1 = []
        check2 = []
        
        def palindromeCheck(node):
            if not node:
                return node
            check1.append(node.val)
            palindromeCheck(node.next)
            check2.append(node.val)
        
        palindromeCheck(head)
        return check1 == check2