class SortandSearch: 
    """
    Well this is my attemp to write MergeSort and QuickSort (using pointers) + BinarySearch all by my own. 
    """
    def main(self, nums, search):
        """ 
        This main function will handle the both the store and the search. 
        The outputs should be the ordered array and the index of the searched value. 
        """
        quicksort_list = self.helper_quick(nums)
        mergesort_list = self.merge_sort(nums)
        sorted_list = mergesort_list
        binary_search = self.binary_search(sorted_list, search)

        return quicksort_list, mergesort_list, binary_search
    
    #### Try with Merge Sort <<<<##################<<<<##################
               
    def merge_sort(self, nums):
        """
        This functions triggers the divide process of the divide and conquer sort algorithm and triggers the recurssion.
        """
                        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        
        left = nums[:mid]
        right = nums[mid:]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        """
        This functions sorts the values and append the remaining ones to the end
        """
        l = 0
        r = 0
        merged = []
        
        while  r < len(right) and l < len(left):
            if left[l]<right[r]:
                merged.append(left[l])
                l += 1
            else: 
                merged.append(right[r])
                r += 1
                
        merged.extend(left[l:])
        merged.extend(right[r:])
        
        return merged

    #### Try with Quick Sort <<<<##################<<<<##################

    def helper_quick(self, nums):
    
        self.quicksort(nums, 0, len(nums)-1)    
        return nums
    
    def quicksort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            
            self.quicksort(nums, low, pivot -1 )
            self.quicksort(nums, pivot +1 , high)
        else: 
            return
    
    def partition(self, nums, low, high):
        
        pivot = nums[high]
        
        i = low
     
        for j in range(low, high): 
            if nums[j]<pivot:
                nums[j], nums[i] = nums[i], nums[j]     
                i+= 1   
                          
        nums[i], nums[high] = nums[high], nums[i]
        
        return i
    
    def binary_search(self, nums, search):

        return self.search_index(nums, search, 0, len(nums)-1)
    
    def search_index(self, nums, search, left, right):
        
        if left > right:
            return -1  # Standard to indicate 'not found' in binary search
        
        mid = (left + right) // 2  
                
        if nums[mid] == search: 
            return mid
    
        if nums[mid] > search:
            return self.search_index(nums, search, left, mid - 1)
        else: 
            return self.search_index(nums, search, mid + 1 , right)
        
    
list = [8,4,6,7,5,4,3,1]
solution = SortandSearch()
sorted_list = solution.main(list, 55)
print("Quicksorted:", sorted_list[0])
print("Mergesorted:", sorted_list[1])
print("Binary Search Result:", sorted_list[2])