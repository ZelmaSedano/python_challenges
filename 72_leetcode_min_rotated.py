https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def truncate_str(str, num):
    # edgecase: if string is empty or num is negative
    if not str or str.isspace():
        return 'please add letters to string'
    if num < 0:
        return 'please only use positive numbers'

    return str[0:num] + '...'

print(truncate_str('hello', 3))
