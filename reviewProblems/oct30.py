# insertion sort 
def insertionSort(arr):
    n = len(arr)
    i = 0 
    for i in range(1, n):
        j = i - 1 
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1 
    
    return arr


# number of students unable to eat lunch 
def lunch(students, sandwiches):
    from collections import deque 
    stuQ = deque(students)
    sandQ = deque(sandwiches)
    while stuQ and sandQ and sandQ[0] in stuQ:
        if stuQ[0] != sandQ[0]:
            student = stuQ.popleft() 
            stuQ.append(student)
        else:
            stuQ.popleft()
            sandQ.popleft() 
    
    return len(stuQ)

# koko eats bananas 
import math 
def eatBananas(piles, h):
    lo = 1 
    hi = max(piles)
    while lo <= hi:
        k = (lo + hi) // 2 
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        if hours <= h:
            result = min(result, k)
            hi = k - 1 
        else:
            lo = k + 1 
    
    return result

# reverse a linked list (iteratively)
def reverse(head):
    prev = None 
    next = None 
    curr = head 
    while curr:
        next = curr.head 
        curr.next = prev 
        prev = curr 
        curr = next 
    
    return prev

# merge sort 
def merge(arr, start, mid, end):
    LEFT = arr[start:mid + 1]
    RIGHT = arr[mid + 1:end + 1]
    i = 0
    j = 0
    k = start 

    while i < len(LEFT) and j < len(RIGHT):
        if LEFT[i] < RIGHT[j]:
            arr[k] = LEFT[i]
            i += 1 
        else:
            arr[k] = RIGHT[j]
            j += 1 
        k += 1 
    
    while i < len(LEFT):
        arr[k] = LEFT[i]
        i += 1 
        k += 1 
    
    while j < len(RIGHT):
        arr[k] = RIGHT[j]
        j += 1 
        k += 1 
    
    return arr
    pass 
def mergeSort(arr, start, end):
    if end - start + 1 <= 1:
        return arr 
    
    # calculate mid 
    mid = (start + end) // 2 

    # sort left 
    mergeSort(arr, start, mid)
    # sort right 
    mergeSort(arr, start, mid + 1)

    # merge
    merge(start, mid, end)

    return arr 