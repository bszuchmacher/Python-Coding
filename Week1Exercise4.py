#  is_parsable(input)
# a) Possible types for input are int or string
# b) If input is of type int or if input can be parsed return true
# c) If input is not int or string or can not be parsed as int return false


# RENDERS TRUE:

def is_parsable():
    try:
        int(2)
        print("True")
    #     IF THE INT OR FLOAT NUMBER (2) IS CHANGED TO "HELLO" OR "COOKIE", IT WOULD RETURN BACK AS FALSE.
    except:
        print("False")
#         SINCE I USED (2) AS THE INT OR FLOAT NUMBER AND NOT A WORD OR VARIABLE WHICH COULDNT CONVERT TO STRING, IT RETURNS
#         AS TRUE. IF I DIDNT...AND USED A WORD, IT WOULD COME BACK AS FALSE. ATTACHED IS THE CODE THAT WOULD RUN BACK
#         AS FALSE

is_parsable();


# RENDERS FALSE:

def is_parsable():
    try:
        int("COOKIE")
        print("True")
    #     IT WOULD RETURN BACK AS FALSE. BECAUSE THE WORD COOKIE HAS NO NUMERICAL OR STRING VALUE
    except:
        print("False")
#       IT WOULD RETURN BACK AS FALSE. BECAUSE THE WORD COOKIE HAS NO NUMERICAL OR STRING VALUE

is_parsable();