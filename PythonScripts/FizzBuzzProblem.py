# FizzBuzz problem
# Write a program that prints the numbers from 1-100 but for multiples of 3 print 'Fizz" instead of
# the number, for multiples of 5 print 'Buzz' and for multiples of 3 and 5 print 'FizzBuzz'

for x,y in enumerate(range(1,101)):
    if y%3 == 0:
        if y%5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif y%5 == 0:
        print('Buzz')
    else:
        print(y)