while True:
    phone_book = {
        "Alice": "9123456789",
        "Bob": "9234567890",
        "Charlie": "9345678901",
        "David": "9456789012",
        "Eva": "9567890123",
        "Frank": "9678901234",
        "Grace": "9789012345",
        "Hank": "9890123456",
        "Ivy": "9912345678",
        "Jack": "9923456789",
        "Kathy": "9934567890",
        "Leo": "9945678901",
        "Mona": "9956789012",
        "Nina": "9967890123",
        "Oscar": "9978901234",
        "Paul": "9989012345",
        "Quinn": "9990123456",
        "Rita": "9991234567",
        "Sam": "9992345678",
        "Tina": "9993456789"
    }
    print("press 1 for read contact\n")
    print("press 2 for edit number or name\n")
    print("press 3 for del a contact\n")
    print("press 4 to see all contacts\n")
    print("Press 5 to Exit from phone_book\n")
    a=int(input("enter a number: \n"))
    if a==1:
        x=input("enter name: ")
        if x in phone_book:
            print(phone_book[x])
        else:
            print("no contact")
    elif a==2:
        y=int(input("press one for edit number or press two to edit name= "))
        if y==1:
            name=input("enter name to edit phone number: ")
            if name in phone_book:
                print(phone_book[name])
                number=input("Enter new number: ")
                phone_book[name]=number
                print("success fully completed")
            else:
                print("No name found")
        elif y==2:
            name=input("enter name: ")
            if name in phone_book:
                new_name=input("enter new name: ")
                phone_book[new_name]=phone_book.pop(name)
                print(phone_book[new_name])
        else:
                print("No name found")
    elif a==3:
            contact=input("enter contact name for delete: ")
            if contact in phone_book:
                del phone_book[contact]
                print("deleted success fully: ")
            else:
                print("no contact found")
    elif a==4:
        print("All Contacts: \n",phone_book)
    elif a==5:
        break
    else:
        print("You entered Wrong option Please enter Correct option: ")
        
        
        
