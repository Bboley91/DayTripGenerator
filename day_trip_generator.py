import random
Destination_list = ['Chicago_Illinois', 'VirginiaBeach_Virginia', 'Kalamazoo_Michigan']
Random_destination = random.choice(Destination_list)
Transportation_list = ['By plane', 'By bus' 'By train']
Random_transportation = random.choice(Transportation_list)
Restaurants_list = ['Burger King', 'Taco Bell', 'Jimmy Johns']
Random_restaurant = random.choice(Restaurants_list)
Entertainment_list = ['A museum', 'A car show', 'A concert']
Random_entertainment = random.choice(Entertainment_list)


welcome_greeting = 'Hello, I am your day trip advisor.' 'I am here to help make your vacation plans go as smoothly as possible.'
print(welcome_greeting)
print('')
print('The destination we have picked for you is', Random_destination, '.', 'Does that sound good for you?')

