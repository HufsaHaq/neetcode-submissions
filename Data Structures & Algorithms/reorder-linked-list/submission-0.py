# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        '''length = self.length(head) 

        count = 0
        itr = head

        while itr:
            if count % 2 ==0: #even
                self.insert_at_index(head,length-1,itr.val)
                length -= 1
            else:
                self.insert_at_index(head,count,itr.val)

            itr = itr.next

        print(head)


    def length(self, listinput):
        count = 0
        itr = listinput
        while itr:
            count += 1
            itr = itr.next

        return count


    def insert_at_index(self,listinput,index,value):
        count = 0
        itr = listinput
        while itr.next:
            if count - 2 == index:
                itr.next.val = value
                break
            count += 1
            itr = itr.next '''




    