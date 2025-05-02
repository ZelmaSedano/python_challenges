def longest_word(string):
    # do you need to remove all spaces, between spaces, or trailing spaces?
    # - you can't remove all spaces, b/c you're counting longest word
    # test to see if between spaces show up
    # removing trailing spaces would be a good idea
    string1 = string.strip()

    longest = ''

    # .split(' ') takes care of the BETWEEN spaces
    for word in string1.split(' '):
        if len(word) > len(longest):
            longest = word

    return len(longest)

print(longest_word('hi             there'))
