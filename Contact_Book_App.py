contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter your choice = ')

    if choice == '1':
        name = input('Enter name = ')
        if name in contacts:
            print(f'Contact name {name} already exists')
        else:
            age=input('Enter Contact age = ')
            mobile=input('Enter Mobile Number = ')
            contacts[name]={'age':int(age),'mobile':mobile}
            print(f'Contact name {name} has been created successfully')

    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {age}, Mobile: {mobile}')
        else:
            print('Contact not found')

    elif choice == '3':
        name = input('Enter contact name to update = ')
        if name in contacts:
            age=input('Enter Update age = ')
            mobile=input('Enter Update Mobile Number = ')
            contacts[name]={'age':int(age),'mobile':mobile}
        else:
            print('Contact not found')
    
    elif choice == '4':
        name = input('Enter contact name to Delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact Name {name} has been deleted succesfully')
        else:
            print('Contact not found')

    elif choice == '5':
        search_name = input('Enter contact name to Search = ')
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
               print(f'Found - Name: {name}, Age: {age}, Mobile:{mobile}') 
               found=True
        if not found:
            print('No contact found with that name')

    elif choice == '6':
        print(f'Total contact in your book {len(contacts)}')

    elif choice == '7':
        print('Good bye....closing program')
        break
    else:
        print('Invalid Input')
