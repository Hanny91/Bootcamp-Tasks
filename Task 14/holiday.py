# Takes in the destination and duration of a trip to calculate the cost

import csv

city_flight = input("What european city are you travelling to?: ")
num_nights = int(input("How many nights do you want to stay?: "))
rental_days = int(input("How many days do you want to rent a car for?: "))

# Functions to calculate each cost
def hotel_cost(num_nights):
    return num_nights * 25

def plane_cost(city_flight):
    city_found = False
    # Searches through the csv doc for an airport in the user's choice of city
    with open("Busiest-European-Airports-2021.csv") as airport_doc:
        airport_dict = csv.DictReader(airport_doc, delimiter=",")
        for row in airport_dict:
            if city_flight.lower() == row['City served'].lower():
                city_found = True
                price = float(row["Change 2021-2020-%"].strip("%").replace(",", ".")) 
                return price
        # Prints a message if the chosen city isn't in the csv doc.
        if city_found == False:
            print("That city isn't served by an available airport.")
            return None 

def car_rental(rental_days):
    return rental_days * 30

# Calculates the total cost of the holiday
def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    total_cost = hotel + plane + car
    return round(total_cost, 2)

# Prints the total cost of the holiday given the city is in the csv doc
if plane_cost(city_flight) is not None:
    print(f"The cost of your holiday will be of: £{holiday_cost(num_nights, city_flight, rental_days)}")
    print(f"""
          Your flight will cost £{plane_cost(city_flight)},
          your hotel will cost £{hotel_cost(num_nights)} 
          and your car rental will cost £{car_rental(rental_days)}""")

