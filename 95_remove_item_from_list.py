def remove_element_from_list(lst, target):
    result = []

    for i in lst:
        if i != target:
            result.append(i)

    return result

print(remove_element_from_list([1,2,3,4], 3))
