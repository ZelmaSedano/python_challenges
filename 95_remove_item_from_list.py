def remove_element_from_list(lst, target):
    result = []

    for i in lst:
        if i != target:
            result.append(i)

    return result

print(remove_element_from_list([1,2,3,4], 3))

# more elegent way
def remove_element_list(lst, element):
    lst.remove(element)

    return lst

print(remove_element_list([1,2,3,4], 3))
