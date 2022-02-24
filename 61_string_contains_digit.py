def containsDigit(str):
    for character in str:
        if character.isdigit():
            return True


print(containsDigit('hi 3'))
