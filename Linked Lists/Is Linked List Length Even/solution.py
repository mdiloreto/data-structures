class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        next_node = head.next
        count = 0
        if head == None: 
            return True
        while next_node != None:
            count=+1
            next_node = next_node.next
        if count % 2 != 0:
            return True
        else: 
            return False