# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        check = {}

        while current:
            if current.__hash__ in check.keys():
                return True
            check[current.__hash__] = 0
            current = current.next
        
        return False