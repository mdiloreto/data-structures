def merge_sort(values):
    """
    Sorts a list in ascending order 
    Returns a new sorted list

    1. Divide: Find the midpoint position of the list and divide into sublists.
    2. Conquer: Recursivly sort the sublists created in the prevous step
    3. Combine: Merge the sortted sublists created in the previous step
    
    """
    
    if len(values) <= 1:
        return values

    left_values, right_values= split(values)
    left = merge_sort(left_values)
    right = merge_sort(right_values)
    
    return merge(left, right)

    
def split(values):

    """
    This function will devide the array in two 
    """
    mid_index = (len(values)) // 2 
    mid_value = values[mid_index]
    left_values = []
    right_values = []
    count = 0

    left_values = values[:mid_index]
    right_values = values[mid_index:]
           
    # while count <= len(values) -1:
    #     if count < mid_index:
    #         left_values.append(values[count])
    #     else:
    #         right_values.append(values[count])
    #     count += 1
    return left_values, right_values

def merge(left, right):
    
    i = 0
    j = 0
    sorted_values = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_values.append(left[i])
            i += 1
        else: 
            sorted_values.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_values.append(left[i])
        i+=1
    
    while j < len(right):
        sorted_values.append(right[j])
        j += 1    
            
    return sorted_values

def check_sorted(values):
    count = 0
    result = True
    while count < len(values) -1 and result == True: 
        if values[count]< values[count + 1]:
            count += 1
            result = True
        else: 
            result = False
            count += 1 
    return print(result) 

def revised_check_sorted(values):
    for i in range(len(values)):
        if values[i] > values[i + 1]:
            return False
    return True

def recursive_check_sorted(values):
    """
    
    """
    n = len(values)
    if n == 0 or n == 1: 
        return True
    return values[0] < values[1] and recursive_check_sorted(values[1:])

values = [23,5,6,123,10,22]
sorted_values = merge_sort(values)
print(sorted_values)

recursive_check_sorted(values)
recursive_check_sorted(sorted_values)