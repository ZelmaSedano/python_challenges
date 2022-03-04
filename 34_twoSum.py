# two sum should only return one pair of numbers
def two_sum(list, target=None):
    if not list:
        raise Exception('please add elements to list')
    if target is None:
        raise Exception('please add 2nd argument')

    # loop through list i times, then j times
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [list[i], list[j]]

    # backup
    return 'there are no numbers that add up to target'

print(two_sum([1,2,3,4], 5))
