from locations import *
from env import api_weather
import urllib.request
import json
import os 


# function for empyting cache file on startup
# file_path = "cache.json"
# if os.stat(file_path).st_size == 0:
#     print("file is empty")
# else:
#      print("File is not empty, clearing")
#      time.sleep(2)
#      with open('cache.json', 'w') as outfile:
#         json.dump('', outfile)

# The link could be modified so no need for new functions
def day_forecast_dl(location_key, api_key):
    day_forecastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key+"?apikey="+api_key+"&details=true&metric=true"
    with urllib.request.urlopen(day_forecastUrl) as day_forecastUrl:
        data = json.loads(day_forecastUrl.read().decode())
    with open('cache.json', 'w') as outfile:
        json.dump(data, outfile)
    print("check json")
    
def gather_json(cachefile):
    with open(cachefile, 'r') as json_file:
        data = json.load(json_file)
    return data

#day_forecast_dl('51097', api_weather())

time.sleep(1)

#print(gather_json('cache.json'))


#for key1 in day_forecast('51097', api_weather)['DailyForecasts']:
#    print("Weather forecast for:"+key1['Date'])
#    print("Min temp: "+str(key1['Temperature']['Minimum']['Value']))
#    print("Max temp: "+str(key1['Temperature']['Maximum']['Value']))
#    print("Forecast: "+str(key1['Day']['ShortPhrase']))
#    print("*****************************************")
