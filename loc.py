# Working but not able to generalise the concept for all the searched queries.Although getting correct for few ..
# The code has been written by Mohammad Amir Jamil. 
# Need to generalise the concept of Location Identifier. 
# This could be used to link the KML file and Tracking System for an Individual.
# If u need to reverse the search i.e. Query search for coordinates, that is also possible but it requires the exact Query String. 
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Khurais Mall Riyadh")
print((location.latitude, location.longitude))
print(location.address)

#Generatign Google Earth KML file using the coordinates .. 
#will try to find a way to automate entry of coordiantes for generating the KML file.

import simplekml
kml = simplekml.Kml()
kml.newpoint(name="amir",coords=[(location.longitude,location.latitude)])
kml.save("coordinate.kml")



