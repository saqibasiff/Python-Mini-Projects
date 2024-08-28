
def GymManagement():

    print('''
            " Welcome To 'AZ Gym Control Centre' "
                                      
    Please Select Option To Continue Processing :

          1 - Register Member :
          2 - Check In :
          3 - Members :
          4 - Exit
''')
    choice = int(input("Enter Your Choice = "))

    members = [ ]

    if choice == 1:
        print('''
        " Please Register Your Name! " ''')
        name = str(input("\nPlease Enter Your Name = "))
        age = int(input("Please Enter Your Age = "))
        fee = int(input("Please Enter Your Fee = "))
        id = int(input("Please Enter Your Gym ID = "))

        print(f"\n\tNew Member '{name}' Is Registered In 'AZ Gym' \n")
        members.append(name)

    elif choice == 3:
        print('''
         What Do You Want To Check About Members ?
              1. Members List :
''')
        choice = int(input("Enter Your Choice = "))

        if choice == 1:
            print(members)
                          
    elif choice == 2:
        
        name2 = str(input("Enter Your Name To Check In = "))

        members.append(name2)


    elif choice == 4:

        print('''Do You Want To Exit The Application ?
              Yes : Press 1''')
        if choice == 1:
           print("Thanks For Using The Application! ")


GymManagement()

