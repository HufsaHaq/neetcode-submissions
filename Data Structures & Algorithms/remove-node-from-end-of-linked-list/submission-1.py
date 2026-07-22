# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            itr = head
            count = 0 
            length = self.length(head) 
            index = length - n 

            if n >= length:
                index = (n - length) 

            print(index)

            if length ==1 or index == 0:
                return head.next

            prev = None
            while itr:
                if count == index:
                    prev.next = itr.next
                    break
                prev = itr
                itr = itr.next
                count += 1

            return head

    def length(self,listinput):
        count = 0 
        itr = listinput
        while itr:
            count += 1
            itr = itr.next

        return count