import re

def check_string_substring(string, substring):
    # edgecases: if string and substring are empty
    if not string and not substring:
        return 'Please add letters to both arguments'
    # if string is empty
    if not string:
        return 'Please add letters to first argument'
    # if substring is empty
    if not substring:
        return 'Please add letters to second argument'

    # if substring is present in string
    if re.search(substring, string):
        return True
    else: 
        return False

print(check_string_substring('hello', 'he'))
