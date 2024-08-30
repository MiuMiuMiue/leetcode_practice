# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 0
        countB = 0

        nodeA = headA
        nodeB = headB
        while nodeA or nodeB:
            if nodeA:
                countA += 1
                nodeA = nodeA.next
            if nodeB:
                countB += 1
                nodeB = nodeB.next
        
        count = countA - countB
        if count < 0:
            while count != 0:
                headB = headB.next
                count += 1
        else:
            while count != 0:
                headA = headA.next
                count -= 1
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next