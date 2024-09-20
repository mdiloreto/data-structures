##### Linear Search
# Linear search scans each element in the list one by one from the beginning until the desired element is found or the end of the list is reached. 
# It works on both sorted and unsorted lists.

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
arr = [5, 3, 8, 6, 7]
target = 6
result = linear_search(arr, target)
print("Element found at index:", result)  # Output: Element found at index: 3 

##### Binary Search
# Binary Search
# Binary search is more efficient but requires that the list is already sorted. 
# It works by repeatedly dividing the search interval in half. 
# #If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. 
# Otherwise, narrow it to the upper half. This process is repeated until the target value is found or the interval is empty.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            return mid
    return "Number not found"

# Example usage
arr = [3, 5, 6, 8, 11]  # Note the array must be sorted for binary search
target = 17
result = binary_search(arr, target)
print("Element found at index:", result)  # Output: Element found at index: 2
