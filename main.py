from cProfile import run
import random 

destinations = ['Canada', 'Japan', 'Sweden', 'Australia']

restaurants = ['KFC', 'McDonalds', 'Pizza Hut', 'Burger King']

mode_of_transportations = ['Bicycling', 'Personal car', 'Skateboarding', 'Walking']

entertainments = ['Movies', 'Clubs', 'Amusement parks', 'Sky diving']

random_destination = random.choice(destinations)

random_restaurants = random.choice(restaurants)

random_mode_of_transportations = random.choice(mode_of_transportations)

random_entertainments = random.choice(entertainments)

print("Welcome to your random day trip generator!")
print("Here are your choices for today:")

#Random Day Trip Generator

def run_day_trip_generator (): 
    print(f"Destination: {random_destination}")
    print(f"Restaurant: {random_restaurants}")
    print(f"Transportation: {random_mode_of_transportations}")
    print(f"Entertainment: {random_entertainments}")

def reselection_process ():
    change_selection = input("Which option would you like to change? Destination, Restaurant, Transportation, or Entertainment? ")
    if change_selection == "Destination":
        global random_destination
        random_destination = random.choice(destinations)
        print(random_destination)
        satisfied_user()
    elif change_selection == "Restaurant":
        global random_restaurants
        random_restaurants = random.choice(restaurants)
        print(random_restaurants)
        satisfied_user()
    elif change_selection == "Transportation":
        global random_mode_of_transportations
        random_mode_of_transportations = random.choice(mode_of_transportations)
        print(random_mode_of_transportations)
        satisfied_user()
    elif change_selection == "Entertainment":
        global random_entertainments
        random_entertainments = random.choice(entertainments)
        print(random_entertainments)
        satisfied_user()
    else:
        print("Invalid answer, please choose: Destination, Restaurant, or Entertainment.")
    
def satisfied_user():
    satisfied_user = input("Are you satisfied with your selection? yes or no: ")
    if satisfied_user == "no":
        reselection_process()
    elif satisfied_user == "yes":
        completed_day_trip()
    else:
        print("Sorry, I don't understand that answer. Please enter yes or no:")

def completed_day_trip():
        print("Your trip is complete!")
        print(f"Your destination is: {random_destination}")
        print(f"Your restaurant is: {random_restaurants}")
        print(f"Your transportation method is: {random_mode_of_transportations}")
        print(f"Your form of entertainment is: {random_entertainments}")

run_day_trip_generator()
satisfied_user()




