s = input('Enter a number. ')
a = s.split()
numbers = []
i = 0
while i < len(a):
    a_i = int(a[i])
    numbers.append(a_i)
    i += 1
i = 0
while i < len(numbers):
    if numbers[i] % 5 == 0 and numbers[i] % 3 == 0:
        print('FizzBuzz')
        i += 1
    elif numbers[i] % 3 == 0:
        print('Fizz')
        i += 1
    elif numbers[i] % 5 == 0:
        print('Buzz')
        i += 1
    else:
        print(numbers[i])
        i += 1
# used while loop from max_v4 to allow any number of entries
