import requests
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


payload = requests.get('http://api.open-notify.org/iss-now.json')
#answer = payload.content.decode("utf-8")
answer = payload.json()
#print(type(answer))   #dict
#Tumkur lat = 13.339168 long = 77.113998
mylat = 13.339168
mylon = 77.113998

lat = float(answer['iss_position']['latitude'])
lon = float(answer['iss_position']['longitude'])

r= haversine(mylon,mylat,lon,lat)
print(r)
