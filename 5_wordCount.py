def wordCount(str):
    #edgecase
    if len(str) == 0:
        return 'please add some words to your string'

    return len(str.split(' '))

print(wordCount('hi there'))
