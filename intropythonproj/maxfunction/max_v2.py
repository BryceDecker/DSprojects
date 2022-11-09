s = input("Please input two numbers separated by a space ")
numbers = s.split()
#print(numbers)
print("The larger number is ", max(int(numbers[0]), int(numbers[1])))
#must take integer value of each index, o/w reads each character