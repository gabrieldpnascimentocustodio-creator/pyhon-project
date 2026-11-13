contacts=[]




def addcontact():
    name_input = input("Enter a name!\n")
    email_input= input("Enter a email!\n")
    phone_input=input("Enter a phone number!\n")

    contacts_dict = {
        "name":name_input,
        "email":email_input,
        "phone":phone_input
    }

    contacts.append(contacts_dict)

def showcontact():
    if not contacts:
        print("Contact list is empty")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"Contact number list {index}")
        print(f"Name: {contact["name"]}")
        print(f"Email: {contact["email"]}")
        print(f"Phone: {contact["phone"]}")

def deleteitem(index):
    if not contacts:
        print("Contact number is empty!\n")
        return

    contacts.pop(index)


while True:
    print("1.Add Item in List Contatc!")
    print("2.Show the Contact list!")
    print("3.Remove item from the list!\n")
    print("0.Exit the programin!\n")
    choice = input("Choose 0 a 3!\n")

    if choice == "1":
        addcontact()

    if choice == "2":
        showcontact()

    if choice == "3":
        index = int(input("Enter a index item you like a remove!\n"))
        deleteitem(index)

    if choice == "0":
        print("Exit the programn!")
        break


