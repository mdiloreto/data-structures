class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
                
    def mergeSort(self, nums):
        if len(nums) <= 1 :
            return nums 

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)             
        
        return self.merge(left, right)

    def merge(self, left, right):
        merge = []
        r = 0
        l = 0
        ## Conditions for merging
        while r < len(right) and l < len(left):
            if left[l]<right[r]:
                merge.append(left[l])
                l += 1
            else:
                merge.append(right[r])
                r += 1
        # Append remaining elements from either left or right
        merge.extend(left[l:])
        merge.extend(right[r:])
        return merge