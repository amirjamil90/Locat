# Working but not able to generalise the concept for all the searched queries.Although getting correct for few ..

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
kml.save("amir.kml")

