def merge(nums1, m, nums2, n) :
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        else:
            while nums2[p2] <= nums1[p1] and p1 >= 0:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            nums1[p] = nums2[p2]
            p2 -= 1
    print(nums1)

# merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# merge([2,3,0,0,0], 2, [2,5,6], 3)
merge([2,0], 1, [1], 1)


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         p1 = m - 1
#         p2 = n - 1
#         p = m + n - 1
#
#         while p2 >= 0:
#             if nums2[p2] > nums1[p1]:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#                 p -= 1
#             else:
#                 while nums2[p2] < nums1[p1] and p1 >= 0:
#                     nums1[p] = nums1[p1]
#                     p1 -= 1
#                     p -= 1
#                 nums1[p] = nums2[p2]
#                 p2 -= 1