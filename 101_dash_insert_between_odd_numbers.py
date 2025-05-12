def convert_string_to_list(string):
    # create an empty list to hold numbers
    result = []


    for i in range(len(string)):
        # Keep as string for easy joining
        result.append(string[i])
        # if the current element is less than the last element of the string
        if i < len(string) - 1:
            # convert the current and next number to an integer
            current = int(string[i])
            next_num = int(string[i+1])
            # see if they're odd
            if current % 2 == 1 and next_num % 2 == 1:
                # if they are odd, add a dash
                result.append('-')

    # return joined dashed string                
    return ''.join(result)

print(convert_string_to_list('37373'))  # Output: "3-7-3-7-3"
