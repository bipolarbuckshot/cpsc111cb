#!usr/bin/env python3
#Carson Black
#Midterm_Project_Carson_Black.py


'''
This project took several hours of research and made me learn how to use
several python mechanics that I either did not know how to use, or in
some cases, did not know existed before this (such as 'with'). I also
added the ability to save and load from a file, and vCard support.
Overall, this took waaaaaay too long. Not due to lack of understanding
or anything, more just because I got bored and wanted to add a bunch
of stupid extra features and make things pretty. Enjoy the almost 200
lines of code I hereby bestow upon you!

PS I'm a huge fan of camelCase, underscores are annoying to type so
many times!
'''


import os # Used for clearing the console. This is needed to determine the OS of the user, because Windows in weird. :P
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
# If you see something like {tc.R}, that means the following text inside the f-string will be printed red, while {tc.x} resets the color.

# 'def' defines a user-made function. I have used it to make 8 functions, of which the last one is the main function that calls the other 7.

def clearConsole(): # begin function clearConsole.
    if os.name == "nt": # nt is Windows
        os.system("cls")
    else:               # everything else can be assumed to be either MacOS or Linux.
        os.system("clear")
# end function clearConsole.


def mainMenu(): # This literally only exists because I got tired of copying and pasting. It also looks way better.
    input(f"\n{tc.Y}Press enter to go back to the main menu...{tc.x}\n")


def saveContact(): # begin function saveContact.
    with open(FILENAME, "w") as contactsFile: # "w" is write mode.
        json.dump(contacts, contactsFile, indent=4) # dumps contents of the 'contacts' variable into whatever 'contactsFile' was defined as, see line above.
        # indent=4 forces "pretty printing" with 4 spaces per indentation, because I got tired of the entire json being on 1 line. You're welcome in advance.
# end function saveContact.


def addContact(): # begin function addContact.
    
    clearConsole()
    print(f""\
        f"{tc.B}┌────────────────────────────────────────────────┐\n"\
        f"│{tc.G}Enter information as requested to add a contact.{tc.B}│\n"\
        f"└────────────────────────────────────────────────┘{tc.x}\n")
    name = input(f"Enter {tc.B}full name{tc.x}: ") # These ask for inputs to enter into the list.
    birthday = input(f"Enter {tc.Y}birthday{tc.x} in ISO 8601 format (e.g. {tc.Y}1999{tc.x}-{tc.G}01{tc.x}-{tc.R}30{tc.x}): ")
    address = input(f"Enter {tc.R}address{tc.x}: ")
    phone = input(f"Enter {tc.G}phone{tc.x} in E.164 format (e.g. {tc.Y}+1{tc.G}415{tc.R}5552671{tc.x}): ")

    contact = { # here is the list.
        "name": name, # the string is the key, the variable is the value of the key. (key-value pair)
        "birthday": birthday, # these are for later when I need to export a vCard among other things.
        "address": address,
        "phone": phone
    } 

    contacts.append(contact)
    saveContact()
    print(f"{tc.G}New contact named {tc.B}{name}{tc.G} was added.{tc.x}\n")
    mainMenu()
# end function addContact.


def searchContacts(): # begin function searchContacts.
    
    clearConsole()

    category = input(f"Search by {tc.B}name{tc.x}, {tc.Y}birthday{tc.x}, {tc.R}address{tc.x}, or {tc.G}phone{tc.x}. \nEnter a category to search.\n: ")

    if category not in ["name", "birthday", "address", "phone"]:
        print(f"<([  {tc.R}Invalid search category.{tc.x}  ])>\n")
        mainMenu()
        return # ends the function searchContacts and returns to the beginning, starting over.
    
    searchValue = input(f"Enter {category} to search for a contact.\n: ")
    contactFound = False # defining variable
    clearConsole()

    for contact in contacts: # loops through every contact

        if searchValue.lower() in contact[category].lower(): # if the information stored in the searched category is the same as one of the contacts, print the contact and break the loop.
            # The .lower() method on both sides makes the search case-insensitive, which is convenient.
            print(f""\
                f"{tc.B}┌──────────────┐\n"\
                f"│{tc.G}Contact Found.{tc.B}│\n"\
                f"└──────────────┘{tc.x}\n"\
                f"{tc.B}Name{tc.x}: {contact["name"]} \n{tc.Y}Birthday{tc.x}: {contact["birthday"]}"\
                f"\n{tc.R}Address{tc.x}: {contact["address"]} \n{tc.G}Phone{tc.x}: {contact["phone"]}\n")

            contactFound = True
            continue

    if contactFound: # if no matching contact is found, print a message and move on.
        mainMenu()
    else:
        print(f"{tc.R}No contacts found.{tc.x}\n\n")
        mainMenu()
# end function searchContacts.


def export_vCard(contact): # begin function export_vCard for contact.
    names = contact["name"].rsplit(" ", 1) # Splits the first and last names starting from the right at the first space. (Accounts for multiple first names.)
    firstName = names[0]
    lastName = names[1] if len(names) > 1 else "" # if the length of the list "names" is at least 2 (implying there is a first and a last name), set lastName to the second value in names.
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
    print(f"{tc.G}vCard saved as {tc.B}{os.path.abspath(filename)}{tc.G}.{tc.x}") # Another useful thing from "os". Prints file path to console. (It should be clickable!)
    mainMenu()
# end function export_vCard.


def exportContact(): # begin function exportContact.
    clearConsole()
    if not contacts: #                          If there are no contacts,
        print("There are no saved contacts.") # print this,
        mainMenu()
        return #                                then go back.
    else:
        print("Saved contacts:\n")
    for i, contact in enumerate(contacts):
        print(f"Contact {i+1}: {contact["name"]}") # i+1 converts internal python numbers (list starting at value 0) to human readable numbers (starting at 1).
    try:
        selection = int(input(f"\n{tc.Y}Enter contact number to export.{tc.x}\n: ")) - 1 # Converts entry back from human numbers to internal python numbers starting at 0.
        if selection in range(len(contacts)):
            export_vCard(contacts[selection])
        else:
            print(f"<([  {tc.R}Contact number outside range provided. Try again.{tc.x}  ])>\n")
            mainMenu()
    except ValueError:
        print("Enter a valid number from the list.\n: ")
# end function exportContact.


def addressBook(): # begin function addressBook.
    
    while 1: # A way other than (but functionally the same as) 'while True' to make an endless loop. Will not exit program until user specifies.
        clearConsole()
        print(f"\n  Number of saved contacts: {len(contacts)}")
        funcSelection = input("" \
        f"{tc.B}┌───────────────────────────────────────────┐\n" \
        f"│{tc.x} Enter function: search, add, export, quit {tc.B}│\n" \
        f"└───────────────────────────────────────────┘{tc.x}\n: ")
        # It took a lot of trial and error to get these boxes to look right, so I hope you like them!

        if funcSelection == "search": # These direct the program to a different defined function based on user input.
            searchContacts()
        elif funcSelection == "add":
            addContact()
        elif funcSelection == "export":
            exportContact()
        elif funcSelection == "quit":
            if input("Quit program? y/n\n: ") == "y":
                clearConsole()
                print("Program terminated.")
                break
            else:
                print("Returning to main menu.\n")

        else:
            print(f"<([  {tc.R}Invalid function. Try again.{tc.x}  ])>\n")
# end function addressBook.


addressBook() # Anything starting with def clearConsole all the way to the end of the program is executed with this one line.