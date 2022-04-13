def consecutive_ints(list):
    if not list:
        return 'please add elements to list'
    # return any(list[i] == list[i+1] for i in range(len(list)-1))
    # do not build an iterate over an elements
    for i in range(len(list)-1):
      if list[i] == list[i+1]:
        return True

    return False

print(consecutive_ints([22,23,8,8,8,1]))
