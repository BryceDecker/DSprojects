s = input("Please input numbers separated by a space ")
a = s.split()
numbers = []
i = 0
while i < len(a):
    a_i = int(a[i])
    numbers.append(a_i)
    i += 1
print("The maximum number entered was ", max(numbers))
