def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]    
        return quicksort(left) + middle + quicksort(right)
print(quicksort([5,22,6,53,83,38,37,95,46]))