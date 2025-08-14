import os

FILENAME = "contacts.txt"


def add_contact(name, phone):
    try:
        with open(FILENAME, "a") as f:
            f.write(f"{name},{phone}\n")
        print("Contact added successfully.")
    except Exception as e:
        print("Error while adding contact:", e)


def view_contacts():
    try:
        with open(FILENAME, "r") as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found.")
            for line in contacts:
                name, phone = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts file found.")
    except Exception as e:
        print("Error while reading contacts:", e)


def search_contact(keyword):
    try:
        with open(FILENAME, "r") as f:
            found = False
            for line in f:
                name, phone = line.strip().split(",")
                if keyword.lower() in name.lower() or keyword in phone:
                    print(f"Name: {name}, Phone: {phone}")
                    found = True
            if not found:
                print("No matching contact found.")
    except FileNotFoundError:
        print("No contacts file found.")


while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        n = input("Enter name: ")
        p = input("Enter phone: ")
        add_contact(n, p)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        k = input("Enter name/phone to search: ")
        search_contact(k)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
