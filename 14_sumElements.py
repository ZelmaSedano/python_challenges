def sum_list(list):
    # edgecases: if list is empty
    if not list:
        return 'please add elements to list'

    return sum(list)

print(sum_list([1,2,3,4,5]))
