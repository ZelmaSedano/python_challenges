def checkP(string):
    if len(string) == 0 or 
    
    # create a counter variable
    count = 0

    # loop through string, looking for ( & )
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

    return count == 0

print(checkP('hi'))
