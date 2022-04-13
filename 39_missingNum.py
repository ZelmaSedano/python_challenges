def missing_num(list):
    # check to make sure arr isn't empty
    if not list:
        return 'please add items to your list'
    
    # make sure to start from 0 to last element, otherwise it won't work
    # make a range from 0 to length of the list (no need to use -1)
    # check to see if the value you got out of that iterable if a number in the list
    for i in range(list[0], list[-1]+1):
      # we don't know at what number this range starts - give me the first onein the list
      # range generates an arbritrary iterable
        if i not in list:
            return i

    return 'no missing numbers'

# the range is looking for continuity starting from the beginning and ending of the list by generating a range of numbers that it KNOWS doesn't have any missing numbers
print(missing_num([2,3,4,5,7])) # range is 5 long
# if that i (0) is not in the list, return that number
# range(start, stop, jump)
