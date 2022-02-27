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
    if entry == 1:
       entry = input("What's contact name?")
       if entry in contacts.keys():
            print(entry +" "+ contacts[entry])
       else: print("Contact not found")  