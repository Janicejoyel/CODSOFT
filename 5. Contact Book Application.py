# Contact Book Application 

contact_list = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    contact_list.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contact_list:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contact_list, start=1):
        print(f"\nContact {idx}:")
        print(f"Name   : {contact['Name']}")
        print(f"Phone  : {contact['Phone']}")
        print(f"Email  : {contact['Email']}")
        print(f"Address: {contact['Address']}")

def search_contact():
    search_term = input("Enter Name or Phone to search: ")
    found = False
    for contact in contact_list:
        if contact['Name'] == search_term or contact['Phone'] == search_term:
            print("\n--- Contact Found ---")
            print(f"Name   : {contact['Name']}")
            print(f"Phone  : {contact['Phone']}")
            print(f"Email  : {contact['Email']}")
            print(f"Address: {contact['Address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the Name of the contact to update: ")
    for contact in contact_list:
        if contact['Name'] == name:
            print("Enter new details (leave blank to keep unchanged):")
            phone = input(f"New Phone (current: {contact['Phone']}): ") or contact['Phone']
            email = input(f"New Email (current: {contact['Email']}): ") or contact['Email']
            address = input(f"New Address (current: {contact['Address']}): ") or contact['Address']
            contact.update({"Phone": phone, "Email": email, "Address": address})
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ")
    for contact in contact_list:
        if contact['Name'] == name:
            contact_list.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
