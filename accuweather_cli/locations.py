import urllib.request
import json
import time
from env import api_weather

c = api_weather()
b='Sofia'
a='BG'

ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')

def cityInfo(code, city, api_key):
    search_adress = "http://dataservice.accuweather.com/locations/v1/cities/"+code+"/search?apikey="+api_key+"&q="+city+"&details=true"
    
    with urllib.request.urlopen(search_adress) as search_adress:
        data = json.loads(search_adress.read().decode())
    
    location_key = data[0]['Key']
    return (location_key)

z = cityInfo(a, b, c)


print(z)