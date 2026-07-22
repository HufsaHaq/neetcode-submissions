# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # say we have a linked list 1,2,3,4,5,6
        # if we want [0, n-1, 1, n-2, 2, n-3, ...]
        # the we need to split the list into 2 and pop off the beginning for the first halve amd the ed from the second half
        # first_half = 1,2,3
        # second_half = 4,5,6
        slow, fast = head, head.next  # to find middle we have a fast and slow pointer
        while fast and fast.next:
            slow = slow.next # moves by 1
            fast = fast.next.next # moves by 2 so by the time it goes out of bounds slow is half way through

        second = slow.next
        prev = slow.next = None
        while second: # we need to reverse the links of the secnd list since we need to take off  from th end 
            tmp = second.next
            second.next = prev
            prev = second # og : 4,5,6 new:6,5,4
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




    