def removeDuplicates(nums) -> int:
    i = 0
    j = 0
    duplicated_count = 0
    while i < len(nums):
        while j < len(nums) - 1:
            if nums[j + 1] == nums[i]:
                j = j + 1
                duplicated_count += 1
            else:
                break
        if j < len(nums) - 1:
            nums[i+1] = nums[j+1]
        i += 1
        j += 1
    print(nums)
    return i - duplicated_count

print(removeDuplicates([1,1,1,2,2,2,4,4]))

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         j = 0
#         duplicated_count = 0
#         while i < len(nums):
#             while j < len(nums) - 1:
#                 if nums[j + 1] == nums[i]:
#                     j = j + 1
#                     duplicated_count += 1
#                 else:
#                     break
#             if j < len(nums) - 1:
#                 nums[i + 1] = nums[j + 1]
#             i += 1
#             j += 1
#         print(nums)
#         return i - duplicated_count