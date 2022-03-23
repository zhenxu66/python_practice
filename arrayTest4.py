def removeElement(nums, val: int) -> int:
    occu = 0
    for i in range(len(nums)):
        if nums[i] == val:
            occu += 1
            j = i
            length = 0
            while j < len(nums) - 1:
                if nums[j + 1] == val:
                    occu += 1
                    length += 1
                    j = j + 1
                else:
                    break
            k = i
            while k + length < len(nums) - 1:
                nums[k] = nums[k + length + 1]
                nums[k + length + 1] = '_'
                k += 1

    print(nums)
    return occu




# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         occu = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 occu += 1
#                 j = i
#                 length = 0
#                 while j < len(nums) - 1:
#                     if nums[j + 1] == val:
#                         occu += 1
#                         length += 1
#                         j = j + 1
#                     else:
#                         break
#                 k = i
#                 while k + length < len(nums) - 1:
#                     nums[k] = nums[k + length + 1]
#                     nums[k + length + 1] = '_'
#                     k += 1




print(removeElement([3,3], 3))

