class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.binarySearch(num, 1, num)
    def binarySearch(self, num, l, r):

        if l > r: 
            return False

        mid = l + (r - l) // 2

        if mid * mid == num:
            return True
        elif mid * mid > num:
            return self.binarySearch(num, l, mid -1)
        else: 
            return self.binarySearch(num, mid + 1, r)
