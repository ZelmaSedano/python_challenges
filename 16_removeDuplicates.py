def remove_duplicates(list1):
    # edgecase: if list is empty
    if not list1:
        return 'please add elements to list'

    # remove the duplicates with a set
    return list(set(list1))

print(remove_duplicates([1,2,3,4,4,4,4]))
