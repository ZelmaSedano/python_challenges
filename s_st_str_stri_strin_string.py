def s_st_str(str):
    if not str or str.isspace():
        return 'please add letters to string'

    result = ''

    # you have to add a +1, or it won't go to the end of the string
    for i in range(len(str)+1):
        result += str[0:i]

    return result

print(s_st_str('Code'))
