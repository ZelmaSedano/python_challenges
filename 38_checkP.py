def checkP(str):
    if not str or str.isspace():
        return 'please add some letters to your string'
    # create a counter variable
    count = 0

    # loop through string, looking for ( & )
    for i in str:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

    return count == 0

print(checkP(' '))
