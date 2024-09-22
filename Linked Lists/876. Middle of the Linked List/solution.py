# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        map = {}
        current = head
        count = 0
        while current:
            count += 1
            map[count] =  current
            current = current.next
        return map[(int(count/ 2)) + 1] 