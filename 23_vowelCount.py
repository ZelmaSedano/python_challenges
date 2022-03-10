def vowel_count(str=None):
    if str is None:
        return 'please add a string'
    if not str or str.isspace():
        return 'please add letters to string'
    

    # create a count variable
    count = 0
    # define what a vowel is
    vowels = 'aeiou'
    # lowercase all the letters
    str.lower()

    # loop through str
    for c in str:
        if c in vowels:
            count += 1

    # if count is 0, return no vowels
    if count == 0:
        return 'no vowels'
    # otherwise, return count
    else:
        return count

print(vowel_count())
