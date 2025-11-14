def most_common_letter(string):
    # create a dictionary to push the string & value into
    most_common = {}

    # loop through the string:
    for i in string:
        # if the character already exists in the dictionary, add to its value
        if i in most_common:
            most_common[i] += 1
        else:
            # adds the i element with a value of 1
            most_common[i] = 1

    return max(most_common, key=most_common.get)

print(most_common_letter('hiii'))
