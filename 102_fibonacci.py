def fibonacci_sequence(num):
    a = 0
    b = 1
    while a <= num:
        print(a)
        temp = a  # Store original 'a' value before changing it
        a = b     # New 'a' becomes old 'b'
        b = temp + b  # New 'b' becomes sum of original 'a' + old 'b'

fibonacci_sequence(50)
