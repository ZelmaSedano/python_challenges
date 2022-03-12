# given a string like: THIS_IS_A_STRING, transform in into: This Is A String
def alter_string(str=None):
    # edgecases: if arg empty or str empty
    if str is None:
        return 'please add string to argument'
    elif not str or str.isspace():
        return 'please add letters to string'

    # change the underscores into spaces
    str = str.replace('_', ' ')
    # lowercase all the letters
    str = str.lower()
    # capitalize the first letter of each word
    return str.title()

print(alter_string('THIS_IS_A_STRING'))
