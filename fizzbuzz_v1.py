number = int(input('Enter a number. '))
if number % 5 == 0 and number % 3 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
# had to recognize the 'and' conditional was priority and should be if statement as opposed to elif
# could it be done a different way? could swap first and last line then change top line to !=.
# breaks if invalid format entered (eg "15 22" not int)
