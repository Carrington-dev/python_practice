import re


print("a\ds")

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)


print (re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))