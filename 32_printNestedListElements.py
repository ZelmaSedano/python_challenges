# arr can't be 'list' b/c we're using list to check w/ isinstance - it confuses the computer
def printNested(arr):
    if not arr:
        return 'please add elements to list'
    for i in arr:
        if isinstance(i, list):
            for j in i:
                print(j)
        else:
            print(i)

printNested([1,2,3,[4,5,[6]]])
