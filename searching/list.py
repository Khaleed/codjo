def binary_search(target,listy,size):
    middle = size//2
    upper = size
    lower = 0
    if target == listy[middle]:
        return middle
    while target != listy[middle]:
        if target < listy[middle]:
            upper = middle
            middle = (upper + lower) // 2
        if target >  listy[middle]:
            lower = middle
            middle = (upper + lower) // 2
        if target == listy[middle]:
             return middle
        if middle > size:
             return -1
