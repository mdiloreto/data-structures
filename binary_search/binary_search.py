class BadSolution:
    def search(self, nums: List[int], target: int) -> int:     
        return self.binarySearch(nums, target, 0, len(nums)-1)
    
    def binarySearch(self, nums, target, left, right):
        if left > right: 
            return -1
        
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            return self.binarySearch(nums, target, left, mid - 1)
        else: 
            return self.binarySearch(nums, target, mid +1 , right)
        
class GoodSolution:
    def search(self, nums, target):
        return self.binarySearch(nums, target, 0, len(nums)-1)
    
    def binarySearch(self, nums, target, l, r):
        while l <= r:
            mid = l + ((r-l)//2)
            if nums[mid] < target:
                l = mid + 1
            elif target < nums[mid]:
                r = mid -1 
            else: 
                return mid
        return -1 