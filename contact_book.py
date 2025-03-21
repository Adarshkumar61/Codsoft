# Features in my contact book:
#contact add
#contact view
#contact search
#contact update
#contact delete
contact_list = []

def contact_add(listt):
    try:
        name, phnumber = listt.split()
        contact_list.append([name, phnumber])
    except ValueError:
        print("wrong format..") 

def contact_view():
    if not contact_list:
        print("Empty list..")
    for i, todo in enumerate(contact_list, start=1):
        name, phnumber = todo
        print(f"{i}. Name: {name}\n PhoneNumber: {phnumber}")

def contect_search(search_item):
    found_contact = []
    for todo in contact_list:
        name, phnumber = todo
        if search_item in name:
            found_contact.append(todo)
    if todo:
        print("Search results are: ") 
        for i, todo in enumerate(found_contact, start=1):
            name, phnumber = todo
            print(f"{i}. Name: {name},\n PhoneNumber: {phnumber}")
    else:
        print("No contact has been found of this name")           

def contact_update():
    search_item = input("enter the contact name for updation: ")
    found_contact = None
    for todo in contact_list:
        name, phnumber = todo
        if search_item in name:
            found_contact = todo
            break
    if found_contact:
        print("Enter the updated details for update..")
        name = input("Enter the Updated name: ")
        phnumber = input("enter the updated number: ")
        index = contact_list.index(found_contact)
        contact_list[index] = [name, phnumber]
        print("Contact Updated Succesfully...")
    else:
        print("No contact found with this name..")    

def contact_delete(contact_number):
    try:
        del contact_list[contact_number -1]
    except IndexError:
        print("please enter correct input")

while True:
    print("1. create contact..")
    print("2. View contact..")
    print("3. Search Contact..")
    print("4. Contact delete...")
    print("5. contact update..")
    print("6. for quit contact app..")
    choice = input("Enter what do u want to do (1,2,3,4,5,6): ")
    if choice == "1":
        listt = input("enter details (name, phone number): ")
        contact_add(listt)
    elif choice == "2":
        contact_view()
    elif choice == "3":
        search_item = input("enter name of the contact: ")
        contect_search(search_item)
    elif choice == "4":
        task_number = int(input("enter the contact index you want to delete: "))
        contact_delete(task_number)
    elif choice == "5":
        contact_update()
    elif choice== "6":
        break
    else:
        print("invlaid input choose correct option")