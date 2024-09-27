### how recursion works 

def sum(numbers):
    total = 0 
    for number in numbers: 
        total += number
        
    return total

#### recursion error infinit loop

def sum(numbers):
    remaining_sum = sum(numbers[1:])
    return numbers

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
    
def recursive_check_sorted(values):
    """
    
    """
    n = len(values)
    if n == 0 or n == 1: 
        return True
    left, right = split(values)
    
    left = recursive_check_sorted(left)
    right = recursive_check_sorted(right)
    
    return values[0] < values[1] and recursive_check_sorted(values[1:])

list = [1,7,3,6,8,33,5,7,88,5,9]

left, right = split(list)

print(left, right)

print(recursive_check_sorted(list))
