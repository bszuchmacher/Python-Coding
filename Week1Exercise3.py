# 3) Build function is_even(number)
# a) Returns true if number is even, otherwise false
# b) Number should be integer, if not, display a meaningful msg and exit

def is_even():
    x = input("Please choose a number:   ")
    if x.isdigit():
        if int(x) % 2 == 0:
            print("True")
            exit()
        else:
            print("False")
            exit();
    else:
        print(' YOUR INPUT is not a number, why are you still doing this? Try again.')
        exit()
is_even();
