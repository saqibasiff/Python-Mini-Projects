def calculation():
       
        num1 = int(input(f"Enter Your Number 1 = "))
        num2 = int(input(f"Enter Your Number 2 = "))

        print('''
            Please Enter The Operation You Want To Calculate With :
              
              1. Addition (+)
              2. Subtraction (-)
              3. Multiplication (*)
              4. Division (/)
''')
        choice = input("Please Enter Your Choice = ")

        if choice == "+" or 1:
                result = num1 + num2
                print(f"Your 1st Number '{num1}' & 2nd Number '{num2}' Addition Is = '{result}'")

        elif choice == 2 or "-":
                result = num1 - num2
                print(f"Your 1st Number '{num1}' & 2nd Number '{num2}' Subtraction Is = '{result}'")

        elif choice == 3 or "*":
                result = num1 * num2
                print(f"Your 1st Number '{num1}' & 2nd Number '{num2}' Multiplication Is = '{result}'")

        elif choice == 4 or "/":
                result = num1 / num2
                print(f"Your 1st Number '{num1}' & 2nd Number '{num2}' Division Is = '{result}'")

        else:
              print("GoodBye !")


calculation()

