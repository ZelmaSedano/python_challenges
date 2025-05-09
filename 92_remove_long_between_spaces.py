def remove_long_between_spaces(string):
    # make sure to put space between quotes for join to maintain separate words
    return ' '.join(string.split())

print(remove_long_between_spaces('hi     there'))
