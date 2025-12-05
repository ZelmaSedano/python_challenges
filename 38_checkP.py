def check_p(string):
    # if there aren't any parentheses
    if '(' not in string and ')' not in string:
        return 'no parentheses'
    
    # create a count variable
    count = 0

    # loop through the string
    for i in string:
        if i == '(':
            count+=1 
        elif i == ')':
            count-=1

    # if there are equal parentheses,return x
    return count == 0

print(check_p(''))
