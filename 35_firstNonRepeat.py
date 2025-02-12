# more robust solution
def RepeatingFunc(myStr):
	char_order = []
	counts = {}

	for c in myStr:
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1
			char_order.append(c)
	for c in char_order:
		if counts[c] == 1:
			return c
	return None

# brute forc eapproach
def first_non_repeat(str):
    # loop through the range/string
    # this creates a range/numbers the length of the string
    # range generates a sequence of numbers from 0 to len(string) -1
    for i in range(len(str)):
        if str.count(str[i]) == 1:
            return str[i]

    return 'no non-repeating characters'

print(first_non_repeat('hih'))
