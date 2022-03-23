def validMountainArray(arr) -> bool:
    i = 0
    if len(arr) < 3:
        return False
    while i + 2 < len(arr) :
        if arr[i + 1] > arr[i]:
            i += 1
        elif i == 0:
            return False
        else:
            break

    if arr[i + 1] < arr[i] and i + 1 < len(arr):
        j = i + 1
        if len(arr) == 3:
            return True
        while j + 1 < len(arr) and arr[j + 1] < arr[j]:
            j += 1
        if j + 1 == len(arr):
            return True
        else:
            return False
    else:
        return False


print(validMountainArray([1,7,9,5,4,1,2]))

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        if len(arr) < 3:
            return False
        while i + 2 < len(arr):
            if arr[i + 1] > arr[i]:
                i += 1
            elif i == 0:
                return False
            else:
                break

        if arr[i + 1] < arr[i] and i + 1 < len(arr):
            j = i + 1
            if len(arr) == 3:
                return True
            while j + 1 < len(arr) and arr[j + 1] < arr[j]: # always use the length limit first j + 1 < len(arr)
                j += 1
            if j + 1 == len(arr):
                return True
            else:
                return False
        else:
            return False