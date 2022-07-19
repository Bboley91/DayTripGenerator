import random

Destination_list = ['Chicago_Illinois', 'Virginia Beach_Virginia', 'Kalamazoo_Michigan']
transportation_list = ['by plane', 'by bus', 'by train']
Restaurants_list = ['Burger King', 'Taco Bell', 'Jimmy Johns']
Entertainment_list = ['a museum', 'a car show', 'a concert']


def welcome_message():
    welcome_greeting = 'Hello, I am your day trip advisor.' 'I am here to help make your vacation plans go as smoothly as possible.'
    print(welcome_greeting)

def destionation_selection():
    random_destination = random.choice(Destination_list)
    print(f'The destination we have picked for you is',{random_destination}, '.', 'Does that sound good for you?')
    users_choice = input('yes/no' ' ') 
    while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
        random_destination = random.choice(Destination_list)
        print(f'ok, fortunatly we have other locations available.', 'How about',{random_destination}, 'instead?')
        users_choice = input('yes/no' ' ')
        if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
            print('I am glad i could make the right choice for you!')
            return random_destination

def transportation_selection():
    random_transportation = random.choice(transportation_list)
    print('Now that we have that decided lets choose how you would like to get there.')
    print(f'The mode of transportation we have picked for you is',{random_transportation}, '.', 'Does that sound good for you?')
    users_choice = input('yes/no' ' ') 
    while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
        random_transportation = random.choice(transportation_list)
        print(f'ok, fortunatly we have other modes of transportation available.', 'How about',{random_transportation}, 'instead?')
        users_choice = input('yes/no' ' ')
        if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
            print('I am glad i could make the right choice for you!')
            return random_transportation

def entertainment_selection():
    random_entertainment = random.choice(Entertainment_list)
    print('Now that we have that decided lets choose what you would like to do while you are there.')
    print(f'The destination we have picked for you is',{random_entertainment}, '.', 'Does that sound good for you?')
    users_choice = input('yes/no' ' ') 
    while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
        random_entertainment = random.choice(Entertainment_list)
        print(f'ok, fortunatly we have other locations available.', 'How about',{random_entertainment}, 'instead?')
        users_choice = input('yes/no' ' ')
        if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
            print('I am glad i could make the right choice for you!')
            return random_entertainment

def restaurant_selection():
    random_restaurant = random.choice(Restaurants_list)
    print('Now that we have that decided lets choose where you would like to eat for the afternoon.')
    print(f'The destination we have picked for you is',{random_restaurant}, '.', 'Does that sound good for you?')
    users_choice = input('yes/no' ' ') 
    while users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
        random_restaurant = random.choice(Restaurants_list)
        print(f'ok, fortunatly we have other locations available.', 'How about',{random_restaurant}, 'instead?')
        users_choice = input('yes/no' ' ')
        if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
            print('Outstanding, i am so glad i could help you make your travel plans a little easier today.' 'Now lets confirm your trip.')
            return random_restaurant


# after showing the user their trip you should confirm it one last time, if they say yes confrim say "have a ncie trip"
# elif they say no print "sorry lets try again"
# in the elif you would call run_program() after the print statment
def confirm_trip(confirmed_destination,confirmed_transportation,confirmed_entertainment,confirmed_restaurant):
    print('The trip we have selected for you to day is:')
    print('Destination:',(confirmed_destination))
    print('Transportation:',(confirmed_transportation))
    print('Entertainment:',(confirmed_entertainment))
    print('Restaurant:',(confirmed_restaurant))


def final_trip_confirmation(confirmed_destination,confirmed_transportation,confirmed_entertainment,confirmed_restaurant):
    print('Is this trip satisfactory?')
    users_choice = input('Yes/No')
    if users_choice == 'yes' or users_choice == 'Yes' or users_choice == 'YES' or users_choice == 'y' or users_choice == 'Y':
        print(f'Amazing, you will be going to', {confirmed_destination}, '.', 'You will be traveling',{confirmed_transportation}, '.', 'You will be going to', {confirmed_entertainment}, '.', 'You will be eating at', {confirmed_restaurant},'.')
        print('Have and amazing trip!')
    elif users_choice == 'no' or users_choice == 'No' or users_choice == 'NO' or users_choice == 'n' or users_choice == 'N':
        print('Ok, not a problem we can start over again.')
        run_program
       


    


    def run_program():
        welcome_message()
        confirmed_destination = destionation_selection()
        confirmed_transportation = transportation_selection()
        confirmed_entertainment = entertainment_selection()
        confirmed_restaurant = restaurant_selection()
        confirm_trip(confirmed_destination,confirmed_transportation,confirmed_entertainment,confirmed_restaurant)
        
        
        run_program()