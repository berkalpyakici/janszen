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

    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyAAJnnaSI6ivwFneYGiILu700jVWHDfw0c')

    def zipcode_data(self,zipcode):
        """
        Input: An integer representing a zipcode
        Output: A list of grocery stores within the zipcode
        """

        local = []
        location_tuple = ()
        if self.gmaps.geocode(address=str(zipcode)):
            location_data = self.gmaps.geocode(address=str(zipcode))[0]

            lat_long_dict = location_data["geometry"]["bounds"]["northeast"]

            location_tuple = (float(lat_long_dict['lat']),float(lat_long_dict['lng']))

            local = self.gmaps.places_nearby(location=location_tuple,radius=24140,type="supermarket")

        return [local,location_tuple]

    def geolocation_data(self,location_tuple):
        """
        Input: An integer representing a zipcode
        Output: A list of grocery stores within the zipcode
        """
        local = self.gmaps.places_nearby(location=location_tuple,radius=24140,type="supermarket")

        return [local,location_tuple]

    def city_data(self):
        """
        Input: String representing a city's name
        Output: A list of grocery stores within a city
        """
        return ""

    def convert_zip(self,zipcode):
        """
        Input: a zipcode represented as an integer
        Output: the latitude and longitude
        """
        return ""

class grocery():

    #lat, longitude, distance from another grocery object
    #an initializer, a name?
    def __init__(self,latitude=29.756, longitude=95.357):
        self.lat = latitude
        self.long = longitude


#first = new grocery(some_lat, some_long)
#first.within_mile(another_lat, another_long)

#grocery(within_mile(lat))
