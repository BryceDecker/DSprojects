s = input("Please input numbers separated by a space ")
a = s.split()
#print(a)
print('The largest value is ', max(a))
# fails if numbers arent written in form of largest number e.g. says 8 > 15, but 08 < 15. has to do with string?
