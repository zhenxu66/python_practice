import functools
# create list
listA = list(range(1,10,2))
listA_1 = [x**2 for x in range(1,10,2)]

listA_2 = sorted([(1, 304), (2, 101), (2, 104)], key=lambda x: x[-1], reverse=False)
listA_2_2 = sorted([(1, 304, 1111), (2, 101, 2222)], key=lambda x: (x[-2], x[-1]), reverse=False)

listA_3 = list(filter(lambda elem:len(elem) > 4, "this test word length".split(" ")))

listA_4 = [sum((x, y)) for (x, y) in zip([1, 2], [3, 4])]
listA_4 = [x**2 + y**2 for (x, y) in zip([1, 2], [3, 4])]

listA_5 = functools.reduce(lambda x, y: x + y, ['this', 'reduce', 'all'])

listA_6 = list("CHINA")

# modify list
listA.append('average')
listA.append(sum(listA[:-1])/(len(listA)-1))
listA.insert(0, "class A")
listA.extend(('tuple1', 'tuple2'))
listA.extend({'set1', 'set2'})

listB = "this is a list test".strip().split()
listB_1 = [ele.upper() for ele in listB]
listB_1.sort(key=lambda x: x[-1])  # last element order
listB_1.reverse()  # reverse elements

# find in list
print(listA_2.count((2, 101)))
print(listA_2.index((2, 101)))


def main():
    print("hello")

if __name__ == "__main__":
    main()