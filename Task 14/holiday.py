# Takes in the destination and duration of a trip to calculate the cost

import csv

destinations_str = 'Istanbul', 'Moscow', 'Paris', 'Amsterdam', 'Moscow', \
                    'Frankfurt', 'Madrid', 'London', 'Barcelona', 'Saint Petersburg',\
                    'Moscow', 'Paris', 'Palma de Mallorca', 'Munich', 'Athens', \
                    'Lisbon', 'Rome', 'Vienna', 'Zürich', 'Berlin', 'Milan', 'Kyiv', \
                    'Oslo', 'Brussels', 'Copenhagen', 'Málaga', 'Dublin', 'Düsseldorf', \
                    'Stockholm', 'Warsaw', 'London', 'Bucharest', 'Simferopol', 'Nice', \
                    'Milan/Bergamo', 'London', 'Catania', 'Manchester', 'Geneva', 'Porto', \
                    'Alicante', 'Hamburg', 'Heraklion', 'Krasnodar', 'Ibiza', 'London', \
                    'Marseille', 'Naples', 'Budapest', 'Palermo', 'Lyon', 'Prague', 'Milan', \
                    'Helsinki', 'Cologne/Bonn', 'Bologna', 'Valencia', 'Ufa', 'Kaliningrad', \
                    'Kazan', 'Toulouse', 'Charleroi', 'Basel/Mulhouse/Freiburg im Breisgau', \
                    'Stuttgart', 'Thessaloniki', 'Seville', 'Venice', 'Rhodes', 'Sofia', \
                    'Nantes', 'Belgrade', 'Bergen', 'Faro', 'Mineralnye Vody', 'Kraków', \
                    'Bordeaux', 'Edinburgh', 'Samara', 'Anapa', 'Tirana', 'Rostov-on-Don', \
                    'Cagliari', 'Eindhoven', 'Bilbao', 'Malta', 'Minsk', 'Birmingham', 'Riga', \
                    'Katowice', 'Belfast', 'Rome', 'Corfu', 'Pristina', 'Reykjavík', 'Gdańsk', \
                    'Bristol', 'Olbia', 'Paris', 'Glasgow', 'Turin', 'Trondheim'

city_flight = input(f"""
                    {destinations_str}
                    
Which of the cities above are you travelling to?:""")
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

# Prints the total costs of the holiday given the city is in the csv doc
if plane_cost(city_flight) is not None:
    print(f"The cost of your holiday to {city_flight} will be of: £{holiday_cost(num_nights, city_flight, rental_days)}")
    print(f"""
          Your flight will cost £{plane_cost(city_flight)}
          Your hotel will cost £{hotel_cost(num_nights)} 
          Your car rental will cost £{car_rental(rental_days)}""")