x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# 并集
print(x.union(y))

# 交集
# x.intersection_update(y)
# print(x)
print(x.intersection(y))


# 对称差集（去除重叠部分）
# x.symmetric_difference_update(y)
# print(x)
print(x.symmetric_difference(y))


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle= list(set(color))
print(shuffle)