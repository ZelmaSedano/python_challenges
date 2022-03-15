def swap_case(str):
    # edgecase: if string is empty
    if not str or str.isspace():
        return 'please add letters to string'

    return str.swapcase()

print(swap_case('Hi'))
