def consecutive_ints(list):
    if not list:
        return 'please add elements to list'
    return any(list[i] == list[i+1] for i in range(len(list)-1))

print(consecutive_ints([]))
