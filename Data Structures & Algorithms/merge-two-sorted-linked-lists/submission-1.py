# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        a = list1
        b = list2
        dummy = ListNode(0) # dummy start - we'll need to dismiss this head
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a #ListNode(a.val , None)
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next

        tail.next = a or b

        return dummy.next # to dismiss dummy value of 0 at the start