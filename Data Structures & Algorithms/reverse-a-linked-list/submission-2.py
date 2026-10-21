# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive solution
        #time o(n), space o(n)

        if not head:
            return None
        newHead=head
        if head.next:
           newHead= self.reverseList(head.next)
           head.next.next= head #reversing the link btw the next node and the head
        head.next= None
        return newHead


        