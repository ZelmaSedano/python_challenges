def remove_spaces(str):
    # edge case: if str is empty, return message
    if len(str) == 0 or str.isspace():
        return 'please add some words to your string'

    return str.replace(' ', '')

print(remove_spaces('hi mom'))
