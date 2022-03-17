from os import removedirs


def remove_duplicates(list1):
    # edgecase: if list is empty
    if not list1:
        return 'please add elements to list'

    # return a set of the list - sets remove duplicates
    return list(set(list1))

print(remove_duplicates([1,2,3,3,3]))
