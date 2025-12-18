def phonebook(name, phone, email):
    phone_book = {'name': name, 'phone': phone, 'email': email} # you can remove the variable phonebook and directly replace return for cleaner.
    return phone_book

contacts = []

def add_contact():


    f_name = input("name: ")
    p_number = input("mobile number: ")
    e_mail = input("email: ").strip()


    user_info = phonebook(f_name, p_number, e_mail) # call value
    contacts.append(user_info)


def delete_contact():

    print("choose which names would you like to delete.")
    print("------LIST OF NAMES------")

    for index, value in enumerate(contacts):  # using enumerate in a for loop is good for deleting purposes
        print(f"{index}. {value['name']} - {value['phone'][-4:]}")  # especially if you have a duplicate names
        # I put a slice to just reveal the 4 last digit
    delete = int(input("input the users number: "))
    if delete < 0 or delete >= len(contacts):
        print("invalid input")

    else:
        del contacts[delete]# deleting a dictionary about the user
                                # or you can use a temporary variable then add a remove syntax.
                                 # like this temporary_variable = contacts[delete]
                                # then contacts.remove(temporary_variable)
        print("CONTACT DELETED....")

def search_contact():
    search = input("input to find a user: ").lower()
    for contact in contacts:
        if search == contact['name'].lower():
            print(f"{contact['name']}\n{contact['phone']}\n{contact['email']}") # can also use flag just put active False
            break       # then change the break into active True and remove the else statement change it into if not active
    else:
        print("user not found!")

def show_all_contacts():

    print("----CONTACTS-----")
    for contact in contacts:  # this will show all your contacts that have been input and saved.
        print(f"name - {contact['name']}\nmobile - {contact['phone']}\nemail address - {contact['email']}\n-------------")


def edit_contacts():

    print("-----------EDIT INFORMATION----------")
    for contact in contacts:
        print(f"{contact['name']}")
    edit_info = input("enter the name of a user you want to edit: ").lower()

    for contact in contacts:
        if edit_info == contact['name'].lower():
            print(f"name - {contact['name']}\nphone - {contact['phone']}\ne-mail - {contact['email']}")

            new_input = input("which field you want to edit?(type:name/phone/email): ")
            if new_input == 'name'.lower():
                new_name = input("input new name: ").strip()
                contact['name'] = new_name
            elif new_input == 'phone':
                new_phone = input("input new phone: ")
                contact['phone'] = new_phone
            elif new_input == 'email':
                new_email = input("input new email: ").strip()
                contact['email'] = new_email

            print(f"name - {contact['name']}\nmobile - {contact['phone']}\ne-mail - {contact['email']}")
            break

    else:
        print("invalid input")


while True:

    print("------------MY PHONEBOOK-------------")
    print("------------ADD CONTACT-----------")
    print("-----------DELETE CONTACT----------")
    print("----------SHOW ALL CONTACT--------")
    print("----------SEARCH CONTACTS----------")
    print("----------EDIT CONTACTS------------")
    print("\n('q' to quit)")
    print("(shortcut keys 'a' for add contact, 'd' for delete contact, 's' for show all contacts, 'se' for search contact, 'e' for edit contact")
        # the shortcut keys is for testing purposes only.


    menu = input("\nchoose which one you want to access: ").lower()


    if menu == 'add contact' or menu == 'a':
        add_contact()

    elif menu == 'q': # the quit button
        break

    elif menu == 'delete contact' or menu == 'd':
        delete_contact()

    elif menu == 'show all contact' or menu == 's':
        show_all_contacts()

    elif menu == 'search contacts' or menu == 'se':
        search_contact()

    elif menu == 'edit contact' or menu == 'e':

        edit_contacts()
