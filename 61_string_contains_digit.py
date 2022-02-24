def containsDigit(str):
    for character in str:
        if character.isdigit():
            return True
    return False


print(containsDigit('hi'))
