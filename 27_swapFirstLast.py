def swapFirstLastElement(str):
    # edge case:
    if not str or str.isspace():
        return 'please add letters to string'
        
    # split the list into a list of letters
    arr = list(str)

    # flip the first and last letter
    arr[0], arr[-1] = arr[-1], arr[0]

    return ''.join(arr)

print(swapFirstLastElement('hello'))
