import random 

destinations = ['Canada', 'Japan', 'Sweden', 'Australia']

restaurants = ['KFC', 'McDonalds', 'Pizza Hut', 'Burger King']

mode_of_transportations = ['bicycling', 'personal car', 'skateboarding', 'walking']

entertainments = ['Movies', 'clubs', 'amusement parks', 'sky diving']

random_destination = random.choice(destinations)

random_restaurants = random.choice(restaurants)

random_mode_of_transportations = random.choice(mode_of_transportations)

random_entertainments = random.choice(entertainments)

#Random Day Trip Generator

def run_day_trip_generator (): 
    print(random_destination)


run_day_trip_generator()




