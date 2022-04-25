# def findLongest(lst):
#     special = list(set(lst))
#     result = dict(zip(special,[0]*len(special)))
#     for elem in lst:
#         if elem in special:
#             result[elem] += 1
#     return result
#
# print(findLongest(list('aabbcccddddd')))

# def findLongest2(lst):
#     i = 0
#     j = 1
#     unique = list(set(lst))
#     result = dict(zip(unique, [0]*len(unique)))
#     while j < len(lst):
#         if lst[i] == lst[j]:
#             result[lst[i]] += 1
#             j += 1
#         else:
#             i = j
#             j += 1
#
#     arr = list(result.items())
#
#     arr.sort(key = lambda item: item[1])
#
#
#     return arr[-1]
# print(findLongest2(list('aabbcccdddadd')))

def findLongest3(lst):
    # i = 0
    # j = 1
    # count = 1
    # max_count = 1
    max_value = ''
    i, j, count, max_count = 0, 1, 1, 1

    # while j < len(lst):
    #     if lst[j] == lst[i]:
    #         count += 1
    #     else:
    #         if count > max_count:
    #             max_value = lst[i]
    #             max_count = count
    #         i = j
    #         count = 1
    #     j += 1

    for j in range(1, len(lst)):
        if lst[j] == lst[i]:
            count += 1
        else:
            if count > max_count:
                max_value = lst[i]
                max_count = count
            i = j
            count = 1

    return[max_value, max_count]

print(findLongest3(list('aabbbbbbcccddddadd')))



