def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            j = i + 1
            k = 0
            for k in range(len(arr) - 1, j, -1):
                arr[k] = arr[k - 1]
            if j < len(arr):
                arr[j] = 0
            i += 2
        else:
            i += 1
    print(arr)

parameter = [0,4,1,0,0,8,0,0,3]
duplicateZeros(parameter)

