# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp = temp.next
        itr = head
        while itr:
            temp = ListNode(itr.val,temp)
            itr = itr.next

        return temp

    