# Back move, Save current max value by compared with previous max and replace current value with previous max value
def replaceElements(arr):
    if len(arr) == 1:
        arr = [-1]
    else:
        # for i in range(len(arr) - 3, 0, -1):
        #     if arr[i] <= arr[i + 1]:
        #         arr[i] = arr[i + 1]
        #     else:
        #         arr[i - 1] = arr[i]
        #         arr[i] = arr[i + 1]
        i = len(arr) - 2
        max1 = max(arr[i], arr[i + 1])
        arr[i] = arr[i + 1]
        i -= 1
        while i >= 0:
            temp = max1
            max1 = max(arr[i], max1)
            arr[i] = temp
            i -= 1
        arr[len(arr) - 1] = -1
    return arr

# print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([56903,18666,60499,57517,26961]))


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr = [-1]
        else:
            # for i in range(len(arr) - 3, 0, -1):
            #     if arr[i] <= arr[i + 1]:
            #         arr[i] = arr[i + 1]
            #     else:
            #         arr[i - 1] = arr[i]
            #         arr[i] = arr[i + 1]
            i = len(arr) - 2
            max1 = max(arr[i], arr[i + 1])
            arr[i] = arr[i + 1]
            i -= 1
            while i >= 0:
                temp = max1
                max1 = max(arr[i], max1)
                arr[i] = temp
                i -= 1
            arr[len(arr) - 1] = -1
        return arr