def checkP(str):
    # edge case: make sure string isn't empty or is just empty spaces
    if len(str) == 0 or str.isspace():
        return 'please add some words to your string'
        #throw error instead?
    
    # create a count variable
    count = 0

    # loop through str, adding to count if current element is '(', and subtracting is it's ')'
    for i in str:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

    return count == 0

print(checkP('()('))
