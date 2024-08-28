students = []

def entry():
    name = input("\nEnter Student's Name = ")
    students.append(name)
    print(f"Student '{name}' has been added!")

def display():
    if students:
        print(f"\nThe List Of Students Is:\n{students}")
    else:
        print("No students in the list.")

def delete():
    if students:
        students.clear()
        print("The student's list has been deleted!")
    else:
        print("No students to delete.")

def search():
    student_name = input("Enter Student's Name To Search = ")
    if student_name in students:
        print(f"{student_name} is present in the student's list!")
    else:
        print(f"{student_name} is not found in the list.")

def update():
    old_name = input("Enter The Name You Want To Update = ")
    if old_name in students:
        new_name = input("Enter The New Name = ")
        students[students.index(old_name)] = new_name
        print(f"Student's name updated from {old_name} to {new_name}!")
    else:
        print(f"{old_name} is not found in the list.")

def main():
    print('''
    Welcome To School Management!
            What Do You Want To Select:
    1. Student Entry
    2. Display Students
    3. Delete List
    4. Search List
    5. Update List
          ''')
    
    select_choice = int(input("Enter Choice = "))
    
    if select_choice == 1:
        entry()
    elif select_choice == 2:
        display()
    elif select_choice == 3:
        delete()
    elif select_choice == 4:
        search()
    elif select_choice == 5:
        update()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()