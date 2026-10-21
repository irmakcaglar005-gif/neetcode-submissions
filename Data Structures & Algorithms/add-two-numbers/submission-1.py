# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#edge case1: sizes of linked lists are different
#edge case2: 7+8 dont forget the carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        cur= dummy

        carry=0
        #Keep going while there's still a node in either list or we still have a carry.
        while l1 or l2 or carry:
            #Get the current digits. If one linked list has already ended, treat its digit as 0
            digitlist1= l1.val if l1 else 0
            digitlist2= l2.val if l2 else 0 
        
            #new digit
            val= digitlist1 + digitlist2 + carry
            #15
            carry=val//10
            val=val%10 #ones place
            cur.next=ListNode(val)

            #update ptrs
            cur=cur.next
            #Move both input pointers forward, if they still exist.
            l1= l1.next if l1 else None
            l2= l2.next if l2 else None
        #return 8+7
        return dummy.next