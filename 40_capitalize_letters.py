def capitalize_words(str):
    if not str or str.isspace():
        return 'please add letters to string'

    return str.title()

print(capitalize_words('hi there'))
