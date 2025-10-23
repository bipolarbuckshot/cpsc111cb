#!usr/bin/env python3
#Carson Black
#Midterm_Project_Carson_Black.py


'''
This project took several hours of research and made me learn how to use
several python mechanics that I either did not know how to use, or in
some cases, did not know existed before this (such as 'with'). I also
added the ability to save and load from a file, and vCard support.
'''


import json # Using json library to save and load files. Contacts will be saved between different instances of using this program.
FILENAME = "CarsonBlack_MidtermContactBook.json"

try:
    with open(FILENAME, "r") as contactsFile: # FILENAME is not the same as filename. "r" means read mode.
        contacts = json.load(contactsFile)
except FileNotFoundError:
    contacts = [] # Defines empty list to add contacts to, if there is no existing file containing saved contacts.

# 'class' is basically a way to contain multiple values or lists within one callable variable, in this case 'tc'.

class tc: # Defining a class for text colors later on. 'tc' stands for text color. To be used with f strings.
    R = '\033[91m' # Red
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    B = '\033[94m' # Blue
    x = '\033[0m'  # reset code

# 'def' defines a user-made function. I have used it to make 3 functions, of which the last one is the main function that calls the other 2.

def saveContact(): # begin function saveContact.
    with open(FILENAME, "w") as contactsFile: # "w" is write mode.
        json.dump(contacts, contactsFile, indent=4) # dumps contents of the 'contacts' variable into whatever 'contactsFile' was defined as, see line above.
# end function saveContact.


def addContact(): # begin function addContact.
    
    name = input(f"Enter {tc.B}full name{tc.x}: ") # These ask for inputs to enter into the list.
    birthday = input(f"Enter {tc.Y}birthday{tc.x} in ISO 8601 format [<YYYY-MM-DD>]: ")
    address = input(f"Enter {tc.R}address{tc.x}: ")
    phone = input(f"Enter {tc.G}phone{tc.x} in E.164 format +[country code][local number] (country code for US is 1): ")

    contact = { # here is the list.
        "name": name, # the string is the key, the variable is the value of the key. (key-value pair)
        "birthday": birthday,
        "address": address,
        "phone": phone
    } 

    contacts.append(contact)
    saveContact()
    print(f"New contact named {name} was added.\n")
# end function addContact.


def searchContacts(): # begin function searchContacts.
    
    category = input(f"Search by {tc.B}name{tc.x}, {tc.Y}birthday{tc.x}, {tc.R}address{tc.x}, or {tc.G}phone{tc.x}. \nEnter a category to search.\n: ")

    if category not in ["name", "birthday", "address", "phone"]:
        print("Invalid search category.\n")
        return # ends the function searchContacts and returns to the beginning, starting over.
    
    searchValue = input(f"Enter {category} to search for a contact.\n: ")
    contactFound = False # defining variable

    for contact in contacts: # loops through every contact

        if searchValue in contact[category]: # if the information stored in the searched category is the same as one of the contacts, print the contact and break the loop.
            # print(f"Contact found.\n{contact}")
            print(f"Contact Found. \n{tc.B}Name{tc.x}: {contact["name"]} \n{tc.Y}Birthday{tc.x}: {contact["birthday"]} \n{tc.R}Address{tc.x}: {contact["address"]} \n{tc.G}Phone{tc.x}: {contact["phone"]}\n")
            contactFound = True
            continue

    if not contactFound: # if no matching contact is found, print a message and move on.
        print("No contacts found.\n\n")
# end function searchContacts.


def export_vCard(contact): # begin function export_vCard for contact.
    names = contact["name"].rsplit(" ", 1) # Splits the first and last names starting from the right at the first space. (Accounts for multiple first names.)
    firstName = names[0]
    lastName = names[1] if len(names) > 1 else "" # if/else inside variable definition
    vCard = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{lastName};{firstName};;;\n"
        f"FN:{contact["name"]}\n"
        f"BDAY:{contact["birthday"]}\n"
        f"ADR;TYPE=HOME:;;{contact["address"]}\n"
        f"TEL;TYPE=CELL:{contact["phone"]}\n"
        "END:VCARD\n"
    ) # It was impossible type in the vCard formatting without googling it, but that isn't strictly part of the assignment, so I figure that's fine.
    filename = f"{contact["name"].replace(" ", "_")}.vcf"
    with open(filename, "w") as vCardFileName:
        vCardFileName.write(vCard)
    print(f"vCard saved as {filename}.")
# end function export_vCard.


def exportContact(): # begin function exportContact.
    if not contacts:
        print("There are no saved contacts.")
        return
    print("Saved contacts:\n")
    for i, contact in enumerate(contacts):
        print(f"Contact {i+1}: {contact["name"]}") # i+1 converts internal python numbers (list starting at value 0) to human readable numbers (starting at 1).
    try:
        selection = int(input("Enter contact number to export.\n: ")) - 1 # Converts entry back from human numbers to internal python numbers starting at 0.
        if selection in range(len(contacts)):
            export_vCard(contacts[selection])
        else:
            print("Contact number outside range provided. Try again.\n")
    except ValueError:
        print("Enter a valid number from the list.\n: ")
# end function exportContact.


def addressBook(): # begin function addressBook.
    
    while 1: # A way other than (but functionally the same as) 'while True' to make an endless loop. Will not exit program until user specifies.
        print(f"Number of saved contacts: {len(contacts)}")
        funcSelection = input("Enter function: search, add, export, quit\n: ")
        
        if funcSelection == "search": # These direct the program to a different defined function based on user input.
            searchContacts()
        elif funcSelection == "add":
            addContact()
        elif funcSelection == "export":
            exportContact()
        elif funcSelection == "quit":
            quitConfirmation = input("Quit program? y/n\n: ")
            if quitConfirmation == "y":
                print("Program terminated.")
                break
            else:
                print("Returning to main menu.\n")

        else:
            print("Invalid function. Try again.\n")
# end function addressBook.


addressBook() # Anything starting with def saveContact all the way to the end of the program is executed with this one line.