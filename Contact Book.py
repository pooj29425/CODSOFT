class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
            return
        print("\nContact List:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower() or 
                search_term in contact.phone):
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name
            contact.phone = phone
            contact.email = email
            contact.address = address
            print("Contact updated successfully!")
        else:
            print("Invalid contact index!")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Deleted contact: {deleted_contact.name}")
        else:
            print("Invalid contact index!")

def main():
    book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
            
        elif choice == '2':
            book.view_contacts()
            
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = book.search_contact(search_term)
            if found_contacts:
                print("\nFound Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}")
                    print(f"Phone: {contact.phone}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}\n")
            else:
                print("No contacts found!")
                
        elif choice == '4':
            book.view_contacts()
            try:
                index = int(input("Enter the number of contact to update: ")) - 1
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                book.update_contact(index, name, phone, email, address)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '5':
            book.view_contacts()
            try:
                index = int(input("Enter the number of contact to delete: ")) - 1
                book.delete_contact(index)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '6':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()