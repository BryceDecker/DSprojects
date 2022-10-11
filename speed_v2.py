s = input("Enter driver's speed. ")
if s == '':
    quit()
speed = int(s)
if speed < 70:
    print("Ok.")
elif speed >= 70:
    dem_pts = (speed - 70)//5
# pythoncheatsheet.org to learn about // for integer division
    print("Points: ", dem_pts)
    if dem_pts >= 12:
        print('License suspended.')
# fixed so if enter is pressed script ends