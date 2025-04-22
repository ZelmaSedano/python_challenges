def missing_num(list):
    # I originally used the 'for i in list' loop, BUT that will result in an error when it reaches the end of the list
    for i in range(len(list)):
        if list[i+1] != list[i]+1:
            return list[i]+1
        
print(missing_num([1,2,5]))
