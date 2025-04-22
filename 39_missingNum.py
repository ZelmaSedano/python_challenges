def missing_num(list):
    for i in range(len(list)):
        if list[i+1] != list[i]+1:
            return list[i]+1
        
print(missing_num([1,2,5]))
