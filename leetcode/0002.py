# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node  = ListNode(0)
        dummy = node
        while l1 or l2:
            total_node  = dummy.val
            if l1:
                # print(l1.val)
                total_node +=l1.val
                l1 = l1.next
            if l2:
                total_node +=l2.val
                l2 = l2.next
            dummy.val = (total_node%10)
            if l1 or l2 or total_node>9:
                dummy.next = ListNode(total_node//10)
                dummy = dummy.next
        return (node)



