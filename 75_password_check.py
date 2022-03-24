# import regex
import re

def validate(password):
    if not password or password.isspace():
        return 'please add a number, upper and lower-case letter'
    if re.search('[0-9]',password) is None:
        print("Make sure your password has a number in it")
    if re.search('[a-z]',password) is None: 
        print('Make sure your password has a lower-case letter in it')
    if re.search('[A-Z]',password) is None: 
        print("Make sure your password has a capital letter in it")
    if re.search('[~`!@#$%^&*()-_=+[]\:;"<,>.?]', password) is None:
        print("Make sure your password has a symbol in it")
    else:
        print("Your password seems fine")

validate('Hello1\|')
