# list_square_even_power_odd(list_range) :
# a) Use list comprehension
# b) All even indices will get the square root of their index
# c) All odd indices will get the ^2 of their index
# d) Verify range is relevant


import math

out_long = []
out_compac = []


def list_square_even_power_odd():
    for i in range(16):
        yield i


print([(math.sqrt(i) if (i % 2) == 0 else i ** 2) for i in range(16)])
