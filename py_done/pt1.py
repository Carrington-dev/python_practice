
#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    a_list = list(range(1, n+1))
    for n in a_list:

        # Write your code here
        if n % (3 * 5)  == 0:
            print("FizzBuzz")
        elif n % (3)  == 0:
            print("Fizz")
        elif n % (5)  == 0:
            print("Buzz")
        else:
            print(n)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
