def two_sum(list, target=None):
    if not list:
        return 'please add elements to your list'
    if target is None:
        return 'please add number to 2nd argument'
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [list[i], list[j]]

    return 'no numbers add up to target'

print(two_sum([], 5))
