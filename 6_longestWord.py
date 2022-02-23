def wordCount(str):
    if len(str) == 0:
        return 'please add some letters'
    
    for i in str:
        if len(str) == 1:
            if i == ' ':
                return 'please add letter'

    arr = str.split(' ')
    return len(arr)

print(wordCount('hi there'))
