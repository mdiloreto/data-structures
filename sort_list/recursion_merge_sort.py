def recursion_merge_sort(values):
    sorted_list = []
    
    if len(values) <= 1:
        return values
             
    left, right = split(values)
    
    left = recursion_merge_sort(left)
    right = recursion_merge_sort(right)
    
    sorted_list = merge(left, right)
    
    return print(sorted_list)

def split(values):
    i=0
    left = []
    right = []
    mid = len(values) // 2
    
    while i < len(values)-1:  
        if i < mid:
            left.append(values[i]) 
        elif i >= mid:
            right.append(values[i])
            
        i += 1
    
    return left, right

def merge(left, right):
    i=0
    j=0
    

list = [1,7,3,6,8,33,5,7,88,5,9]

recursion_merge_sort(list)