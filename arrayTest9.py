def sortArrayByParity(nums):
    if len(nums) != 1:
        i = 0
        j = 1
        while j < len(nums) and i < len(nums):
            if nums[i] % 2 == 1:
                if nums[j] % 2 == 1:
                    j += 1
                else:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i += 1
                    j += 1
            else:
                i += 1
                j = i + 1
    print(nums)

# sortArrayByParity([3,1,2,4])
# sortArrayByParity([0,2])
# sortArrayByParity([0,1,2])
# sortArrayByParity([0,2,1,4])