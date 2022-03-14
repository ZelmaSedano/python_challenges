# given a string likst THIS_IS_A_STRING return a string like so: This Is A String
def upstart_alter_str(str):
    # edgecase: if string is empty
    if not str or str.isspace():
        return 'please add letters to string'

    # change all the underscores to spaces
    str = str.replace('_', ' ')

    # lowercase all the letters
    str = str.lower()

    # capitalize the first letters of each word
    return str.title()

print(upstart_alter_str('THIS_IS_A_STRING'))
