def find_minimum_rotated_array(list):
    
    index = list[0]
    
    list = list[index:len(list)] + list[0:index]
    print(list)
    
    return min(list)
    
print(find_minimum_rotated_array([3,2,1,0]))
