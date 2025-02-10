def wordCount(str):
    #edgecase
    if len(str) == 0:
        return 'please add some words to your string'

    # split the string into a list
    list = str.split(' ')

    # return the length of the list
    return len(list)

print(wordCount('hi there'))
