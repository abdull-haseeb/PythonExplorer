def array_reverse(arr):
    start = 0
    end = len(arr) - 1 
    print(a)
    while  start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr
print(array_reverse([5,2,6,2,7,8,6,4]))
