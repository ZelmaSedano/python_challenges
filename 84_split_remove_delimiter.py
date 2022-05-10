def split_remove_delimiter(string):
    # edgecase: if string is empty, tell user to add letters
    if not string:
      return 'please add letters to your string argument'
    
    # use split to remove slashes '/'
    return string.split('/')

print(split_remove_delimiter('hello/there/how/are/you'))
