import random 

destinations = ['Canada', 'Japan', 'Sweden', 'Australia']

restarurants = ['KFC', 'McDonalds', 'Pizza Hut', 'Burger King']

mode_of_transportations = ['bicycling', 'personal car', 'skateboarding', 'walking']

entertainments = ['Movies', 'clubs', 'amusement parks', 'sky diving']

random_destination = random.choice(destinations)

#Random Day Trip Generator

def run_day_trip_generator (): 
    print(random_destination)


run_day_trip_generator()




