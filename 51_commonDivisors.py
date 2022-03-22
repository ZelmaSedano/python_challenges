def leetcode_minimum_rotated(list):
    # define what index we're going to rotate by based off first element
    index = list[0]

    # rotate the list by index #
    # slice off index to end, then add the elements from 0 to index
    # 3,4,5,6,7 --> 6,7,3,4,5
    # 6 = element at index 3 (3=0, 4=1, 5=2, 6=3)
    # 6,7 + 3,4,5 
    result = list[index:len(list)] + list[0:index]

    return min(result)

print(leetcode_minimum_rotated([3,4,5,6,7]))
