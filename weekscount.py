week = int(input("Enter Total Days To Calculate Weeks = "))

if week < 8:
    print("These Days Consist Of 1 Week!")

elif week < 15:
    print("These Days Consist Of 2 Weeks!")

elif week < 22:
    print("These Days Consist Of 3 Weeks!")

elif week < 29:
    print("These Days Consist Of 4 Weeks!")

else:
    print("These Days Are Above 1 Month!")
    