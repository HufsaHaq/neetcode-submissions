# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#    visited= []
#    itr = head
#    while itr.next:
#        if itr.val in visited:
#            return True
#        visited.append(itr.val) 
#        itr = itr.next
#    return False   

class Solution:
    def lengthoflist(self, head) -> int:
        length = 0
        itr = head
        while itr.next:
            length += 1
            itr = itr.next
        return length   

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        itrA = headA
        itrB = headB
        inter = False
        intersection = None
        m = self.lengthoflist(headA)
        n = self.lengthoflist(headB)

        # the lists need the same number of nodes left to go through
        if m > n:
            diff = m - n
            for i in range(diff):
                itrA = itrA.next
        elif n > m:
            diff = n - m
            for i in range(diff):
                itrB = itrB.next

        # NEED TO COMPARE ITR NOT ITR.VAL
        while itrA:
            if itrA is itrB:
                intersection = itrA
                break
            itrA = itrA.next
            itrB = itrB.next

        return intersection
        #If they  intersect,THEN The tail ends of both lists ARE THE EXACT SAME
        







        '''
        while itrB.next:
            if itrA.val == itrB.val and itrA.next.val == itrB.next.val:
                if inter == True:
                    continue
                else:
                    intersection = itrA.next

            if itrA.val != itrB.val and itrA.next.val == itrB.next.val:
                itrA = itrA.next
            if itrA.next and not itrB.next:
                itrA = itrA.next
                continue
            itrB = itrB.next
        '''
        
        return intersection