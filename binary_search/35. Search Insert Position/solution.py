class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)
    def binarySearch(self, nums, target, left, right):
        if left > right: 
            return max(left, right)
        
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            return self.binarySearch(nums, target, left, mid - 1)
        else: 
            return self.binarySearch(nums, target, mid +1 , right)