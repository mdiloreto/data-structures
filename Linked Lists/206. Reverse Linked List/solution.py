# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(head) -> ListNode:
        current = head
        previous = None
        while current:
            prev_next = current.next # Save old next value ref.
            current.next = previous # To swap the connector from current.next to current.previous
            previous = current # Set current as the previous value of the next iteration. 
            current = prev_next # To do next node as the previous next node
        return previous
    
class Solution: 
    def reverseList(self, head: Optional[ListNode], previous: Optional[ListNode] = None) -> Optional[ListNode]:
        
        if not head:
            return previous
        
        next_node = head.next
        head.next = previous

        return self.reverseList(next_node, head)
