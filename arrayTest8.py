def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) != 1:
        i = 0
        j = 1
        while j < len(nums) and i < len(nums):
            if nums[i] == 0:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i] = nums[j]
                    nums[j] = 0
                    i += 1
            else:
                i += 1
                j = i + 1
                #make sure j always follow i to find most recent none zero, move 0 to back and also shifting right
    print(nums)

# moveZeroes([0,1,0,3,12])
# moveZeroes([2,1])
moveZeroes([4,2,4,0,0,3,0,5,1,0])