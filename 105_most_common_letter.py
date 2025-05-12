def most_common_letter(string):
    letter_count = {}

    for c in string:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1

    return max(letter_count, key=letter_count.get)

print(most_common_letter('hiiiieeeee'))
