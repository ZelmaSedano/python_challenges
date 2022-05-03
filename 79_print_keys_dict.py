def print_keys_dict(dict):
    # edgecase: if dictionary is empty
    if not dict:
        # you have to use print, otherwise this won't show up
        # you can return, but you'd have to call print on line 12 
        print('please add elements to dictionary')
    
    # loop through dictionary using for
    for key in dict:
        print(key)

print_keys_dict({'color': 'blue', 'fruit': 'apple', 'pet': 'dog'})
