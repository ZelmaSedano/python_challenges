def vowel_count(str):
    # create a count variable
    count = 0

    # create a set of vowels
    vowels = set('aeiouAEIOU')

    # loop through the str
    for c in str:
        if c in vowels:
            count += 1

    # backup
    if count == 0:
        return 'no vowels'
    else:
        return count

print(vowel_count('hi'))
