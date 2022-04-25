import time
def productExceptSelf(nums):
    start_time = time.perf_counter()
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i-1] * nums[i -1]
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] = ans[i] * right
        right *= nums[i]
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"it takes {duration:0.8f} s to finish")
    return ans

print(productExceptSelf([1,2,3,4,5,6]))


