# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        current = head
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head