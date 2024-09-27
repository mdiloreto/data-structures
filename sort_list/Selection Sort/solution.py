class SelectionSort: 
    def sort_while(self, arr):
        n = len(arr)-1
        i = 0
        while i < n:
            min = i
            k = i+1
            while k < n:
                if arr[k]<arr[min]:
                    min = k
                k = k + 1
            if arr[min]<arr[i]:
                self.swap(arr, i, min)
            i = i + 1    
            
        return arr

    def sort_for(self, arr):
        n = len(arr)-1
        i = 0
        for i in range(n):
            min = i
            for k in range(i+1, n):
                if arr[k]<arr[min]:
                    min = k
                    
            if arr[min]<arr[i]:
                self.swap(arr, i, min) 
            
        return arr

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
arr = [34, 7, 23, 32, 5, 62, 31, 54, 3, 29, 12, 47, 9, 14, 50, 60, 78, 90, 44, 21, 33, 8, 17, 25, 13, 20, 15, 48, 2, 11, 55, 39, 6, 36, 18, 45, 41, 61, 70, 19, 53, 77, 83, 4, 74, 99]
solution = SelectionSort()
solve = solution.sort_for(arr)

print(solve)