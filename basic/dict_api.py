import collections

# create dict

dictA = dict(collections.Counter(list("testStringtt")))
dictB = dict(zip([3, 2, 1], ['math', 'science', 'computer']))
dictB.update({4: 'language'})


def main():
    print(dictB[1])
    print(dictB)
    for key, value in dictB.items():
        print(f"{key} class name is {dictB[key]}")
        print(f"{key} class name is {value}")

    for key in sorted(dictB):
        print(f"{key} class name is {dictB[key]}")



    # find max values
    my_dict = {'x': 500, 'y': 5874, 'z': 560}

    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

    print('Maximum Value: ', my_dict[key_max])
    print('Minimum Value: ', my_dict[key_min])

    if 'math' in dictB.values():
        print('math in dictB')

    if 3 in dictB:
        print('math in dictB')


if __name__ == "__main__":
    main()