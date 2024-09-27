class BubbleSort:
    """
    1. Bubble Sort:
        - How it works: Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.
        - Best-case performance: O(n) (when the list is already sorted)
        - Average and Worst-case performance: O(n²)
        - Use case: It’s simple but inefficient for large datasets. Good for small datasets or educational purposes.
        - Example: For a list [4, 3, 2, 1], it would perform 6 swaps in total, gradually moving the largest unsorted element to the end of the list.
           [4,3,2,1] -->[3,4,2,1] --> [2,4,3,1] --> [1,4,3,2] --> [2,3,4,2] --> [1,2,4,3] --> [1,2,3,4] 
            ^ ^          ^   ^         ^     ^         ^ ^           ^   ^           ^ ^ 
            i j          i  j+1        i    j+2      i+1 j           i  j+2         i+1 j+2    
    """
    def swap(self, arr, i, j):
        
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
           
    def iterative_loop(self, arr):
        n = range(len(arr)-1)
        for i in n:
            for i in n:
                if arr[i]>arr[i+1]:
                    self.swap(arr, i, i+1)
        return arr

    def recursive_loop(self, arr):
        
        return self.help_recursive(arr, len(arr))

    def help_recursive(self, arr, len):
        ran = range(len-1)
        
        if len == 1: 
            return arr

        for i in ran: 
            if arr[i]>arr[i+1]:
                self.swap(arr, i, i+1)            
        
        return self.help_recursive(arr, len-1)

           
arr = [34, 7, 23, 32, 5, 62, 31, 54, 3, 29, 12, 47, 9, 14, 50, 60, 78, 90, 44, 21, 33, 8, 17, 25, 13, 20, 15, 48, 2, 11, 55, 39, 6, 36, 18, 45, 41, 61, 70, 19, 53, 77, 83, 4, 74, 99]
solution = BubbleSort()
solve = solution.recursive_loop(arr)

print(solve)