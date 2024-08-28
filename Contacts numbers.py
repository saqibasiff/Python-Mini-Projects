contacts = []

def Contacts():
    for contact in contacts:
        name = str(input("Enter Your Name = "))
        phone = int(input("Enter Your Conatct Number = "))
        contacts.append({'name' : name, 'phone' : phone})

    print(f"Contact {name} Is Added!")

Contacts()