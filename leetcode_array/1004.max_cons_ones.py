def longestOnes(nums, K):
    l, r = 0, 0
    zeros = 0
    res = 0

    while r < len(nums):
        if zeros < K:
            if nums[r] == 0:
                zeros += 1
            r += 1
        elif nums[r] == 1:
            r += 1
        else:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(res, r - l)

    return res

print(longestOnes([1,1,0,0,0,1,0], 2))
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
