s = input('Enter number(s); if entering multiple, separate with a space. ')
a = s.split()
numbers = []
t = []
i = 0
while i < len(a):
    a_i = int(a[i])
    numbers.append(a_i)
    i += 1
i = 0
while i < len(numbers):
    if numbers[i] % 5 == 0 and numbers[i] % 3 == 0:
        t_i = 'FizzBuzz'
        t.append(t_i)
        i += 1
    elif numbers[i] % 3 == 0:
        t_i = 'Fizz'
        t.append(t_i)
        i += 1
    elif numbers[i] % 5 == 0:
        t_i = 'Buzz'
        t.append(t_i)
        i += 1
    else:
        t.append(numbers[i])
        i += 1
print(*t, sep=", ")
# googled how to print list in cleaner format
# this version prints the results in a horizontal list format by modifying the while loop to create a cleaner list
# tried to replace while loops with for loops, but run into int not iterable error
