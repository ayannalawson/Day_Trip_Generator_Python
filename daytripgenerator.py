import random


destination_list = ['New York', 'Dubai', 'Shanghai', 'Seoul', 'Quebec City']

restaurant_list = ['Italian', 'Hibachi', 'Red Robbin', 'Pizzeria', 'Mediterranean']

transportation_list = ['Car', 'Motorcycle', 'Limo', 'Bus', 'Train', 'Plane']

entertainment_list = ['Video Gaming', 'Movie Theaters', 'Go Karting', 'Paint Ball', 'Comedy Standup']


def greeting():
    return print("Thank you for using Day Trip Generator to plan your next trip! Happy Travels!")


def random_from_list_generator(list, element_from_list=''):
    index = random.randrange(0, len(list))
    new_element = list[index]
    if new_element != element_from_list:
        return new_element
    else:
        return random_from_list_generator(list, new_element)


# Destination
def get_user_input_destination(random_element_from_list, alt_message_bool=False):
    if alt_message_bool == False:
        user_input = input(f'You have selected {random_element_from_list} as the destination for your trip! Is this okay? yes/no: ')
    else:
        user_input = input(f'We apologoze for the misunderstanding but it looks like you dont want this previous option. We have selected {random_element_from_list} for your next trip. However we believe this can be a good alternative. What do you think? yes/no: ')
    if user_input == 'n':
        random_destination = random_from_list_generator(destination_list, random_element_from_list)
        get_user_input_destination(random_destination, True)
    else:
        return random_element_from_list


# Entertainment
def get_user_input_entertainment(random_element_from_list, alt_message_bool = False):
    if alt_message_bool == False:
        user_input = input(f'You have selected {random_element_from_list} for a reason to have a good time. Is this okay? yes/no: ')
    else:
        user_input = input(f'We apologize for the misunderstanding but it looks like you dont want this previous option. We have selected {random_element_from_list} to find something fun to do. However we believe this can be a good alternative. What do you think? yes/no: ')
    if user_input == 'n' or user_input == '':
        random_entertainment = random_from_list_generator(entertainment_list, random_element_from_list)
        get_user_input_entertainment(random_entertainment, True)
    else:
        return random_element_from_list

# Restaurant
def get_user_input_restaurant(random_element_from_list, alt_message_bool=False):
    if alt_message_bool == False:
        user_input = input(f'You have selected {random_element_from_list} for a great place to eat and enjoy yourself. Is this okay? yes/no: ')
    else:
            user_input = input(f'We apologize for the misunderstanding but it looks like you dont want this previous option. We have selected {random_element_from_list} for your next place to eat. However we believe this can be a good alternative. What do you think? yes/no: ')
    if user_input == 'n' or user_input == '':
        random_restaurant = random_from_list_generator(restaurant_list, random_element_from_list)
        get_user_input_restaurant(random_restaurant, True)
    else:
        return random_element_from_list

# Transportation
def get_user_input_transportation(random_element_from_list, alt_message_bool=False):
    if alt_message_bool == False:
        user_input = input(f'You have selected {random_element_from_list} as your transportation choice. Is this okay? yes/no: ')
    else:
        user_input = input(f'We apologize for the misunderstanding but it looks like you dont want this previous option. We have selected {random_element_from_list} for different places to go around town. However we believe this can be a good alternative. What do you think? yes/no: ')
    if user_input == 'n' or user_input == '':
        random_transportation = random_from_list_generator(transportation_list, random_element_from_list)
        get_user_input_transportation(random_transportation, True)
    else:
        return random_element_from_list

# Finalize Transaction
def finalize_transaction():
    new_line = '\n'
    print(f'Great! Im glad you made your decision! Lets get going!{new_line} Congratulations! You have completed your trip. Now lets see what we got.')
    print(f'The trip you generated for:{new_line} Destination: {destination_chosen} {new_line} Transportation: {transportation_chosen}')
    print(f'Restaurant: {restuarant_chosen} {new_line} Entertainment: {entertainment_chosen} {new_line}')
    would_like_to_finalize_trip = input('Are you sure about this trip? Enter yes/no: ')
    if would_like_to_finalize_trip == 'y':
        handle_final_message()
    else:
        handle_modify_booking()

def handle_final_message():
    print(f'Once you arrive at {destination_chosen} by a {transportation_chosen}.')
    print(f'Then whenever you are hungry you will be able to have directions to the type of {restuarant_chosen} restaurant of your choosing.')
    print(f'After that you will spend the day checking out {entertainment_chosen}')
    print('I hope you enjoy your vacation!')


def handle_modify_booking():
   new_line = '\n'        
   print(f'Oh, so which would you like to change? {new_line} a: destination {new_line} b: transportation {new_line} c: entertainment {new_line} d: restaurant {new_line}')
   user_input = input('Please provide answer here ( a b c or d ):  ')
   if user_input == 'a':
      destination_chosen = get_user_input_destination(random_destination)
      finalize_transaction()
   elif user_input == 'b':
      transportation_chosen = get_user_input_transportation(random_transportation)
      finalize_transaction()
   elif user_input == 'c':
      entertainment_chosen = get_user_input_entertainment(random_entertainment)
      finalize_transaction()
   elif user_input == 'd':
      restuarant_chosen = get_user_input_restaurant(random_restaurant)
      finalize_transaction()

greeting()

random_destination = random_from_list_generator(destination_list)

destination_chosen = get_user_input_destination(random_destination)

random_transportation = random_from_list_generator(transportation_list)

transportation_chosen = get_user_input_transportation(random_transportation)

random_restaurant = random_from_list_generator(restaurant_list)

restuarant_chosen = get_user_input_restaurant(random_restaurant)

random_entertainment = random_from_list_generator(entertainment_list)

entertainment_chosen = get_user_input_entertainment(random_entertainment)

finalize_transaction()
