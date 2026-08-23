# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #[0, n-1, 1, n-2, 2, n-3, ...]

        # 1. get to the midpoint using Floyd's algo
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # this line is what splits the LL 

        # 2. reverse 2nd half 
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = prev
        first = head

        # 3. Merge 1st and 2nd half in consecutive order
        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        


        
