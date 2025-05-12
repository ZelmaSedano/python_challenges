"""
Checks if a number is a perfect square using mathematical properties.
"""
def num_is_square(n):
    if n < 0:
        return False
    return int(n ** 0.5) ** 2 == n

print(num_is_square(16))
