# you have to add = None to work
def convert_f_to_c(num = None):
    # edge case: if num is empty, return a message, cuz 0 is a valid temp
    if num is None:
        return 'please add a temp'

    celsius = (num - 32) * 5/9
    return celsius

print(convert_f_to_c())
