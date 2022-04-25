def missing_num(list):
    for i in range(len(list)-1):
        if list[i+1] != list[i]+1:
            return list[i]+1

print(missing_num([1,2,3,4,6]))
