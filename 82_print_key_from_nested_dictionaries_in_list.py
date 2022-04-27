def get_value_key_in_list_nested_dictionary(list):
    # edgecase: if list is empty
    if not list:
        return 'please add multiple nested dictionaries to list'
    for key in list:
        print(key['color'])

print(get_value_key_in_list_nested_dictionary([{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}, {'color': 'purple', 'fruit': 'apple', 'pet': 'dog'}, {'color': 'red', 'fruit': 'apple', 'pet': 'dog'}, {'color': 'violet', 'fruit': 'apple', 'pet': 'dog'}]))
