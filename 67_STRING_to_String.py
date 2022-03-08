# create a function that takes a capitalized string with underscores and returns a regular string w/ the first letter of each word capitalized
def STRING_to_String(str):
    # edgecase
    if not str:
        return 'please add letters to string'

    # remove all the underscores
    str = str.replace('_', ' ')

    # lowercase all the letters
    str = str.lower()

    # title each word
    return str.title()

print(STRING_to_String('HI_THERE'))
