s = input("Enter driver's speed. ")
try:
    speed = int(s)
    if speed < 70:
        print("Ok.")
    elif speed >= 70:
        dem_pts = (speed - 70)//5
        print("Points: ", dem_pts)
        if dem_pts >= 80:
            print("Stop shooting your radar gun at airplanes Joe... there is not a high scores for points.")
        elif dem_pts >= 12:
            print('License suspended.')
except ValueError:
    t = input("Please enter an integer. ")
    try:
        speed_retry = int(t)
        if speed_retry < 70:
            print("Ok.")
        elif speed_retry >= 70:
            dem_pts = (speed_retry - 70) // 5
            print("Points: ", dem_pts)
            if dem_pts >= 80:
                print("Stop shooting your radar gun at airplanes Joe... there is not a high scores for points.")
            elif dem_pts >= 12:
                print('License suspended.')
    except ValueError:
        print("Invalid format, program terminating...")
        quit()
# stackflow helped identify when input was integer or not "try: val = int(userInput) except ValueError:""
