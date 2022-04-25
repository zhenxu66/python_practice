def uniqueIntegerToZero(n):
    res = []
    if n % 2 == 1:
        res.append(0)

    # left = []
    # right = []
    # for i in range(1, n//2 + 1):
    #     left.append(i)
    # for i in range(1, n//2 + 1):
    #     right.append(-i)
    # res.extend(left)
    # res.extend(right)

    res.extend([i for i in range(1, 1 + n//2)])
    res.extend([-i for i in range(1, 1 + n//2)])

    return res

print(uniqueIntegerToZero(4))

