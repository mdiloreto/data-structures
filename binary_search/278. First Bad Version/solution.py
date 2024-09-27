# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(n, 1, n)
    def binarySearch(self, n, l, r):

        if l == r:
            return max(l,r)

        mid = l + (r - l) // 2

        if isBadVersion(mid) == True:
            return self.binarySearch(n, l, mid)
        else:
            return self.binarySearch(n, mid +1, r)