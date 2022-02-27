contacts = {
     "Spongebob": "123-456-7890",
     "Patrick": "987-654-3210",
     "Sandy": "192-083-4756",
    }

def phonebook():
    print("""
        Electronic Phone Book
        **************************
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit 
        
        """)
phonebook()

while(True):
    entry = int(input("Select Option:"))

    if entry == 1:
       entry = input("What's contact name?")
       if entry in contacts.keys():
            print(entry +" "+ contacts[entry])
       else: print("Contact not found")  
    elif entry == 2:
        contact_name = input("Enter contacts name:")
        phone_number = input("Enter contacts number:")
        contacts[contact_name] = phone_number
        print("Contact added!")
    elif entry == 3:
        entry = input("Which contact would you like to delete?")
        if entry in contacts.keys():
            confirm = input("Are you sure you want to delete contact?")
            if confirm == "Yes":
                contacts.pop(entry)
                print("Contact deleted")
            else: print("Contact not deleted")
        if entry not in contacts.keys():
            print("Contact not found")
