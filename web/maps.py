import googlemaps
from datetime import datetime

#gmaps = googlemaps.Client(key='AIzaSyAAJnnaSI6ivwFneYGiILu700jVWHDfw0c')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
#now = datetime.now()
#directions_result = gmaps.directions("Sydney Town Hall",
                                     #"Parramatta, NSW",
                                     #mode="transit",
                                     #departure_time=now)

class maps():
    """
    Generates list of grocery stores based on an input from the user's search
    """

    def __init__():
        self.gmaps = googlemaps.Client(key='AIzaSyAAJnnaSI6ivwFneYGiILu700jVWHDfw0c')

    def zipcode_data(zipcode):
        """
        Input: An integer representing a zipcode
        Output: A list of grocery stores within the zipcode
        """
        return ""

    def city_data():
        """
        Input: String representing
        Output: A list of grocery stores within a city
        """
        return ""



class grocery():

    #lat, longitude, distance from another grocery object
    #an initializer, a name?
    def __init__(latitude=29.756, longitude=95.357):
        self.lat = latitude
        self.long = longitude




#first = new grocery(some_lat, some_long)
#first.within_mile(another_lat, another_long)

#grocery(within_mile(lat))

print(directions_result)


def fetch_grocery(city):
