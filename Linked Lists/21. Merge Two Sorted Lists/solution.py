# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LoopSolution:
    """
    l1 = [1,3,9]
    l2 = [1,7,8]

    l3 = {1->}    

    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        list3 = ListNode()
        curr = list3

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else: 
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1: 
            curr.next = list1
        else: 
            curr.next = list2

        return list3.next
    

class RecursiveSolution:
    """
    l1 = [1,3,9]
    l2 = [1,7,8]

    l3 = {1->}    

    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):

        # Recursion base cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Recursive case: compare heads of both lists
        if list1.val < list2.val: 
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2