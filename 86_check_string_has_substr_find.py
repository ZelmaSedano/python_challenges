def check_string_has_substring(string, substr):
    if(string.find(substr) == -1):
        return False
    else:
        return True

print(check_string_has_substring('hello', 'he'))
