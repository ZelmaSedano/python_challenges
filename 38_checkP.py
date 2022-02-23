def checkP(str):
    count = 0
    for i in str:
        if i == '(':
            count+=1
        elif i == ')':
            count-=1
    return count == 0

print(checkP('()('))
