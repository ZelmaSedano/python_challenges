def canMakePalindrome(str):
    counts = {}
    for c in str:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    # create an empty list
    oddArr = []
    # loop through obj; if value is odd, add to odd arr
    for c in counts:
        if counts[c] % 2== 1:
            oddArr.append(counts[c])
    return len(oddArr) <= 1

print(canMakePalindrome('mom'))
