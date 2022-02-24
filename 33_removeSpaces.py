def removeSpaces(str):
  if not str or str.isspace():
    return 'please add some words to string'

  return str.replace(' ', '')

print(removeSpaces(' '))
