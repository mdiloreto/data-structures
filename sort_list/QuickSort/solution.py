class Solution:
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums)-1)
        return nums
        
    def quicksort(self, nums, start, end ):
        if start < end:
            pivot = self.partition(nums, start, end)
            self.quicksort(nums, start, pivot - 1)
            self.quicksort(nums, pivot +1 , end)
        else: 
            return

    def partition(self, nums, start, end):

            pivot = nums[end]
            i = start
            for j in range(start, end):
                if nums[j]< pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1    
            nums[i], nums[end] = nums[end], nums[i]
            return i
        
arr = [34, 7, 23, 32, 5, 62, 31, 54, 3, 29, 12, 47, 9, 14, 50, 60, 78, 90, 44, 21, 33, 8, 17, 25, 13, 20, 15, 48, 2, 11, 55, 39, 6, 36, 18, 45, 41, 61, 70, 19, 53, 77, 83, 4, 74, 99]
solution = Solution()
solve = solution.sortArray(arr)

print(solve)