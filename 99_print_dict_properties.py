def print_dict_properties(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print(' ' * indent + f'{key}:')
            print_dict_properties(value, indent + 4)
        else:
            print(' ' * indent + f'{key}: {value}')

sample_dict = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York'
    },
    'scores': [85, 90, 78]
}

print_dict_properties(sample_dict)
