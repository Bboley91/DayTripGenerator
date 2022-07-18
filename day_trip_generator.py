import random
Destination_list = ['Chicago_Illinois', 'Virginia Beach_Virginia', 'Kalamazoo_Michigan']
transportation_list = ['By plane', 'By bus', 'By train']
Restaurants_list = ['Burger King', 'Taco Bell', 'Jimmy Johns']
Entertainment_list = ['A museum', 'A car show', 'A concert']

welcome_greeting = 'Hello, I am your day trip advisor.' 'I am here to help make your vacation plans go as smoothly as possible.'
print(welcome_greeting)
print('The destination we have picked for you is',random.choice(Destination_list), '.', 'Does that sound good for you?')
users_choice = input('yes/no' ' ') 
while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
    print('ok, fortunatly we have other locations available.', 'How about',random.choice(Destination_list), 'instead?')
    users_choice = input('yes/no' ' ')
    if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
        print('I am glad i could make the right choice for you!')
print('Now that we have that decided lets choose how you would like to get there.')
print('The mode of transportation we have picked for you is',random.choice(transportation_list), '.', 'Does that sound good for you?')
users_choice = input('yes/no' ' ') 
while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
    print('ok, fortunatly we have other modes of transportation available.', 'How about',random.choice(transportation_list), 'instead?')
    users_choice = input('yes/no' ' ')
    if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
        print('I am glad i could make the right choice for you!')
print('Now that we have that decided lets choose what you would like to do while you are there.')
print('The destination we have picked for you is',random.choice(Entertainment_list), '.', 'Does that sound good for you?')
users_choice = input('yes/no' ' ') 
while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
    print('ok, fortunatly we have other locations available.', 'How about',random.choice(Entertainment_list), 'instead?')
    users_choice = input('yes/no' ' ')
    if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
        print('I am glad i could make the right choice for you!')
print('Now that we have that decided lets choose where you would like to eat for the afternoon.')
print('The destination we have picked for you is',random.choice(Restaurants_list), '.', 'Does that sound good for you?')
users_choice = input('yes/no' ' ') 
while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
    print('ok, fortunatly we have other locations available.', 'How about',random.choice(Restaurants_list), 'instead?')
    users_choice = input('yes/no' ' ')
    if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
        print('I am glad i could make the right choice for you!')
print('Outstanding, i am so glad i could help you make your travel plans a little easier today.' 'Now lets confirm your trip.')
print('The trip we have selected for you to day is:')
