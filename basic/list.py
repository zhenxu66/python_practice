# sorted(items, key=lambda x:func(x), reverse=True)
# filter(lambda x:func(x), items)

from operator import itemgetter


list_number = [1, 2, 3]
list_combined = ['abc', 'xyz', 'aba', '1221']
list_tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (1, 2)]
list_2d = [[2, 4, 6], [1, 3, 5], [8, 10, 12], [7, 9, 11]]

list_a = [2, 3, 4, 6, 12]
list_b = [4, 10, 12]

list_a_even = [x for x in list_a if x % 2 == 0]
print(list_a_even)


# enumerate with index for each element in a list
for num_index, num_val in enumerate(list_combined):
    print({num_index: num_val})

def check_first_last_equal(items):
    tot = 0
    for item in items:
        if(item[0] == item[-1] and len(item) >= 2):
            tot += 1
    return tot

def order_list_tuple(list_tuple):
    return sorted(list_tuple, key=lambda x: x[-1], reverse=False)

def transpose(lst):
    return list(zip(*lst))

def long_words(n, words):
    return list(filter(lambda elem:len(elem)>n, words.split(" ")))


print(check_first_last_equal(list_combined))
print(order_list_tuple(list_tuple))
print(sorted(list_tuple, key=itemgetter(-1)))
print(set(list_tuple))

print(list_2d)
print(transpose(list_2d))

print(long_words(4, "The quick brown fox jumps over the lazy dog"))

print(bool(set(list_a).intersection(set(list_b))))
overlap = set(list_a).intersection(set(list_b))
print(type(overlap))