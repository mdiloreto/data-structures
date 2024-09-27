def selection_sort1(values):
    sorted_list = []
    min = 0
    while values: 
        min = values[0]
        for value in values:
            if value < min:
                min = value
        sorted_list.append(min)
        values.remove(min)
        
    return print(sorted_list)


def selection_sort2(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return print(sorted_list)
        
def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values [min_index]:
            min_index = i
    return min_index
        
list = [2, 25, 42, 1, 6 , 8, 78, -1]

selection_sort1(list)