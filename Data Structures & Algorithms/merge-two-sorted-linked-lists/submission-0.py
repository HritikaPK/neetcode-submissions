# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newList = ListNode() # dummy node with no value 
        tail = newList
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next

        # pending LLs incase one of the LLs finished but the other remains
        if curr1:
            tail.next = curr1
        elif curr2:
            tail.next = curr2

        return newList.next
            




        