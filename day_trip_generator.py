import random
Destination_list = ['Chicago_Illinois', 'Virginia Beach_Virginia', 'Kalamazoo_Michigan']
Transportation_list = ['By plane', 'By bus' 'By train']
Restaurants_list = ['Burger King', 'Taco Bell', 'Jimmy Johns']
Entertainment_list = ['A museum', 'A car show', 'A concert']

welcome_greeting = 'Hello, I am your day trip advisor.' 'I am here to help make your vacation plans go as smoothly as possible.'
print(welcome_greeting)
print('The destination we have picked for you is',random.choice(Destination_list), '.', 'Does that sound good for you?')
users_choice = input('yes/no' ' ') 
while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO':
    print('ok, fortunatly we have other locations available.', 'How about',random.choice(Destination_list), 'instead?')
    users_choice = input('yes/no' ' ')
    if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES':
        print('I am glad i could make the right choice for you!')



