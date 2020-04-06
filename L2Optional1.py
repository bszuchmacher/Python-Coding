# Build get_roots(first, second, third) :
# a) The function calculates the square root of the function with coefficients
# first (a),second (b) and third (c)
# b) Use lambda function //didn't use lambda though.
# c) Verify that second**2 is bigger than 4*first*third

import math

a = int(input("Enter the number for a: "))
b = int(input("Enter the number for b: "))
c = int(input("Enter the number for c: "))

# This is the quadratic formula below
d = b**b - 4 * a * c

if d < 0:
    print("Your 2nd number b total was smaller than 4x a multiplied by c, this wont work")
else:
    x = (-b + math.sqrt(d)) / (2 * a)
    print("This equation's solution is: ", x)