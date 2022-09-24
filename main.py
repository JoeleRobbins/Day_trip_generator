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


#Random Day Trip Generator

def run_day_trip_generator (): 
    print(f"Destination: {random_destination}")
    print(f"Restaurant: {random_restaurants}")
    print(f"Transportation: {random_mode_of_transportations}")
    print(f"Entertainment: {random_entertainments}")

run_day_trip_generator()

satisfied_user = input("Are you satisfied with your selection?")

if satisfied_user == "no":
    run_day_trip_generator()
else:
    print("Your trip is complete!")
    print(f"Your destination is: {random_destination}")
    print(f"Your restaurant is: {random_restaurants}")
    print(f"Your transportation method is: {random_mode_of_transportations}")
    print(f"Your form of entertainment is: {random_entertainments}")





