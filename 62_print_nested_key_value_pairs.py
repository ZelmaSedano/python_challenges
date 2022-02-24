def print_nested_keys_values(dict):
    for each_key, each_value in dict.items():
        print("Person ID:", each_key)
        
        for each_key in each_value:
            print(each_key + ':', each_value[each_key])

print_nested_keys_values({
    1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
    2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}})
