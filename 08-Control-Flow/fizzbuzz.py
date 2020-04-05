# FizzBuzz is a popular programming problem to test a developer's ability to think logically with code.
# The problem is simple but deceptive.
# Define a fizzbuzz function that accepts a single number as an argument. The function should print every number from 1 to that argument.
# There are a couple caveats.
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# If the number is not divisible by either 3 or 5, just print the number.


def fizzbuzz(num):
    count = 1
    while count < num:
        if count % 3 == 0 and count % 5 == 0:
            print('FizzBuzz')
            count += 1
        elif count % 5 == 0:
            print('Buzz')
            count += 1
        elif count % 3 == 0:
            print('Fizz')
            count += 1
        else:
            print(f'{num}')
            count += 1


fizzbuzz(30)