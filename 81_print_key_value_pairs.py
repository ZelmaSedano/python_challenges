def print_key_value_pairs(dict):
    if not dict:
        # if you use return, it won't show up, b/c you have to print at execution to see return
        print('dictionary is empty')
    for key in dict:
        # key & then value using bracket notation
        print(key, dict[key])

print_key_value_pairs({})
