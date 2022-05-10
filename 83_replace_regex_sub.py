import re
# create a method that replaces a given string with another string

def regex_replace_sub(string):
    # use sub method to replace one string w/ something else
    # result = re.sub(pattern, replace, string, count=0, flags=0)
    result = re.sub('a', 'b', string)
    return result

print(regex_replace_sub('abba'))
