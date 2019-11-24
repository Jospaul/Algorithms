def binarysearch(list, target):
    min = 0
    max = len(list) - 1
    while min <= max:
        guess = int((min + max)/2)
        if list[guess] == target:
            return guess
        else:
            if list[guess] > target:
                max = guess - 1
            else:
                min = guess + 1
    return -1


ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
result = binarysearch(ls, 73)

print("Found prime at index " + str(result))