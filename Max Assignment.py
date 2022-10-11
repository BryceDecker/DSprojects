#Programming with Mosh intro to python in an hour
#Assignments taken from website
#First assignment: Write a function that returns the maximum of two numbers

#v1 completes the task with minimal coding and effort
#v2 streamlines v1 by replacing two prompts with a single prompt. discovered issue with comparing 1 digit and 2 digit
#numbers. able to fix by using indices.
#v3 attempts to extend v2 to any amount of numbers entered, however difficulty with number format and using max function
#identified that input is string type and must be converted to tuple or list? Can not use index fix as index length
#is undetermined
#v4 successfully extends v2 to take in any amount of numbers in any format and determines max
#had to work through issue that int was not iterable, so created while loop to iterate. Had to declare numbers
#as a list instead of tuple- not sure why. Googled how to split string into list learned .split

#on v3&4 attempted to solve issue by having numbers entered in various formats (e.g. 3, 15 or 3 15 or 3,15)