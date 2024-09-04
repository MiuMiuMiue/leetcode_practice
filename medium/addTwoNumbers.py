# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addition(node1, node2, one):
            if not node1 and not node2 and one:
                return ListNode(one)
            elif not node1 and not node2:
                return None
            elif not node1:
                current_sum = node2.val + one
                if current_sum >= 10:
                    current_node = ListNode(current_sum - 10)
                else:
                    current_node = ListNode(current_sum)
                current_node.next = addition(node1, node2.next, current_sum // 10)
            elif not node2:
                current_sum = node1.val + one
                if current_sum >= 10:
                    current_node = ListNode(current_sum - 10)
                else:
                    current_node = ListNode(current_sum)
                current_node.next = addition(node1.next, node2, current_sum // 10)
            else:
                current_sum = node1.val + node2.val + one
                if current_sum >= 10:
                    current_node = ListNode(current_sum - 10)
                else:
                    current_node = ListNode(current_sum)
                current_node.next = addition(node1.next, node2.next, current_sum // 10)
            return current_node
        return addition(l1, l2, 0)