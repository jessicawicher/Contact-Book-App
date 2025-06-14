#this is the Python code for the app

def display_menu():
    print()
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
    print()


def add_contact(contact_book):
    name = input("Insert name: ")
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Insert phone: ")
    email = input("Insert email: ")
    address = input("Insert address: ")
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contact(contact_book):
    name = input("Insert name: ")
    if name in contact_book:
        contact_details = contact_book[name]
        phone = contact_details["phone"]
        email = contact_details["email"]
        address = contact_details["address"]
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"Address: {address}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Insert name: ")
    if name in contact_book:
        contact_details = contact_book[name]
        phone = input("Insert phone: ")
        email = input("Insert email: ")
        address = input("Insert address: ")
        if phone == "":
            contact_details["phone"] = contact_details["phone"]
        elif email == "":
            contact_details["email"] = contact_details["email"]
        elif address == "":
            contact_details["address"] = contact_details["address"]
        else:
            contact_details["phone"] = phone
            contact_details["email"] = email
            contact_details["address"] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input("Insert name: ")
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for name, values in contact_book.items():
            tphone = values["phone"]
            tmail = values["email"]
            taddress = values["address"]
            print(f"Name: {name}")
            print(f"Phone: {tphone}")
            print(f"Email: {tmail}")
            print(f"Address: {taddress}")
            print()


contact_book = {}

while True:
    display_menu()
    menu_choice = input()
    if menu_choice == "1":
        add_contact(contact_book)
    elif menu_choice == "2":
        view_contact(contact_book)
    elif menu_choice == "3":
        edit_contact(contact_book)
    elif menu_choice == "4":
        delete_contact(contact_book)
    elif menu_choice == "5":
        list_all_contacts(contact_book)
    elif menu_choice == "6":
        break
