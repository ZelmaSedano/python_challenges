def f_to_c(num = None):
    if num is None:
        return 'please add number to argument'

    celsius = (num-32)*5/9
    return celsius

print(f_to_c(32))
