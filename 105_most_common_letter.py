def most_common_letter(string):

    # create an empty object/dictionary
    letter={}

    # loop through the string
    for i in string:
        # if the letter is in the dictionary, add to its value
        if i in letter:
            letter[i] += 1
        # if it's not in the dictionary yet, add it and make its value 1
        else:
            letter[i] = 1

    # there might not be a most_common_letter, they may all be equally present
    # use a set, a set doesn't allow duplicates
    if(len(set(letter.values()))) == 1:
        return 'no most-common-letter'

    #max(key=letter.get) === find the key in the dictionary with the highest value
    return max(letter, key=letter.get)

print(most_common_letter('hhii'))
