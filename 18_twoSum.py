def two_sum(list, target=None):
    if not list and target is None:
        return 'please add arguments'
    if not list:
        return 'please add elements to list'
    if target is None:
        return 'please add number to 2nd arguemnt'

    # loop through list once, then twice, skipping i
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [list[i], list[j]]

    # backup
    return 'no numbers from list add up to target'

print(two_sum([], ))
