# Initialize an empty dictionary to store contacts
address_book = {}

# Function to add a new contact
def add_contact(name, address, phone_number):
    address_book[name] = {'address': address, 'phone_number': phone_number}
    print(f"Contact for {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if address_book:
        print("\n--- All Contacts ---")
        for name, details in address_book.items():
            print(f"Name: {name}, Address: {details['address']}, Phone: {details['phone_number']}")
    else:
        print("No contacts found.")

# Function to search for a contact by name
def search_contact(name):
    if name in address_book:
        details = address_book[name]
        print(f"Found: Name: {name}, Address: {details['address']}, Phone: {details['phone_number']}")
    else:
        print(f"Contact with name {name} not found.")

# Function to delete a contact
def delete_contact(name):
    if name in address_book:
        del address_book[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"Contact with name {name} not found.")

# Function to display the main menu
def display_menu():
    print("\n--- Name and Address Book ---")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter contact's name: ")
            address = input("Enter contact's address: ")
            phone_number = input("Enter contact's phone number: ")
            add_contact(name, address, phone_number)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact you want to search for: ")
            search_contact(name)

        elif choice == '4':
            name = input("Enter the name of the contact you want to delete: ")
            delete_contact(name)

        elif choice == '5':
            print("Exiting Address Book...\n Thankyou.!")
            break

        else:
            print("Invalid choice! ")

# Start the program
if __name__ == "__main__":
    main()
