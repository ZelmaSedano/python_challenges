def consecutive_ints(list):
    if not list:
        return 'please add elements to list'
    # return any(list[i] == list[i+1] for i in range(len(list)-1))
    # do not build an iterate over an elements
    for i in list:
      # is the current value the same as the next value
      return i == i

print(consecutive_ints([22,23,8,8,8,1]))
