# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        itr1 = list1
        itr2 = list2
        while itr1 and itr2:
            print(itr1.val)
            print(itr2.val)
            if itr1.val > itr2.val:
                self.add(list3, itr2.val)
                print(list3)
                itr2 = itr2.next
            else:
                self.add(list3, itr1.val)
                itr1 = itr1.next
        
        while itr2:
            self.add(list3, itr2.val)
            itr2 = itr2.next
        
        while itr1:
            self.add(list3, itr1.val)
            itr1 = itr1.next
        
        
        return list3.next # skips the dummy 0 at the start of list 

    def length(self, listinput):    
        itr = listinput
        count = 0

        while itr:
            count += 1
            itr = itr.next
        
        return count

    def add(self,inputlist,value):
        itr = inputlist
        while itr.next:
            itr = itr.next
        itr.next = ListNode(value)

    def remove(self,inputlist,value):
        itr = inputlist
        if itr.val == value:
            itr = itr.next.next
            return

        while itr.next:
            if itr.next.val == value:
                itr.next = itr.next.next
                break
            itr = itr.next 
            
        #for sime reason my return isnt working 




    