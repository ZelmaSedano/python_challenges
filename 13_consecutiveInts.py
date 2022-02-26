def consecutive_ints(list):
    return any(list[i] ==list[i+1] for i in range(len(list)-1))


print(consecutive_ints([1]))
