# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited= []
        itr = head

        while itr.next:
            if itr.val in visited:
                return True

            visited.append(itr.val) 
            itr = itr.next

        return False   
        