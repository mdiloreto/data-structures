"""
Arrays have indexes. [{A:0, B:1, 14:2}]
array[] in python is different.

Python defines both an array and a list type and while they look and feel similar to one another they have their own uses. 
The array.array class in Python is a thin wrapper around a C array and this introduces some limitations. 
For example, Python arrays are homogeneous and can only hold data of a single kind. 
The type does take up much less space in memory than Python lists however so in general you would use an array if space was a concern or if you wanted to expose some C functionality.
Python lists are the more frequently used type and the de facto representation of an array like structure. 
They are a heterogeneous and contiguous data structure.

"""
# Operations for Listsr

List = []
List = [1,2,3,4,5,6]

# Access and read values

Result = List[5]
Result = List[10] ## Error 

# Search for an arbitrary value

## Linear search: 
def linear_search(arr, target):
    """worst way
    for i in range(0, len(lst)):
        if lst[i] == target:
    """

    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

## Binary search 

def binary_search(List, target):
    low, high = 0, len(List) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = List[mid]
        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            return mid
    return "Number not found"

# Insert values at any point into the structure

List.append(1)
List.extend([1,3,56,7])

# Delete values in the structure


