users_list = []

while True:
    print('1. Add new user')
    print('2. Display all users')
    print('3. Display users by age')
    print('4. Remove user by ID')
    print('5. Change status')
    print('6. Exit')

    choice = input('Choose the option: ')

    if choice == '1':
        new_user_id = int(input("Type user's ID: "))
        new_user_name = input("Type user's name: ")
        new_user_age = int(input("Type user's age: "))
        new_user_status = bool(input("Type user's status (True or False): "))
        users_list.append({'id': new_user_id, 'name': new_user_name, 'age': new_user_age, 'status': new_user_status})

    elif choice == '2':
        for user in users_list:
            print(user)

    elif choice == '3':
        def get_age(user):
            return user.get('age')

        users_list.sort(key=get_age)
        print(users_list)

    elif choice == '4':
        id = int(input('Type ID of user you want to delete: '))
        for dict in users_list:
            if dict['id'] == id:
                users_list.remove(dict)
        print(users_list)

    elif choice == '5':
        id = int(input('Type ID of user, whose status you want to change: '))
        for dict in users_list:
            if dict['id'] == id:
                dict['status'] = not dict['status']
        print(users_list)

    elif choice == '6':
        break

    else:
        print('Wrong input, try again')