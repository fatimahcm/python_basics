#importing libraries we use:
import argparse
import requests

#initializing argparser
parser= argparse.ArgumentParser(description='Process weather')
#takes an argument and defines it as location (input)
parser.add_argument('--location', help='enter city')
#bc wtf is args? syntax to wrap user input
args= parser.parse_args()

def weather_parser(location):
    url = "https://www.metaweather.com/api/location/search/?query={}".format(location)
    response = requests.get(url)
    weather_id = response.json()[0]["woeid"]
    weather_url = "https://www.metaweather.com/api/location/{}/".format(weather_id)
    r= requests.get(weather_url).json()['consolidated_weather'][0]
    print ("City:", location)
    print ("Minimum Temperature:", r["min_temp"])
    print ("Maximum Temperature:", r["max_temp"])
    print ("Temperature:", r["the_temp"])
    print ("Humidity:", r["humidity"])

#defining user input as args (defined line 10) and location (input defined in ln8)
new = (args.location)
#gotta call the dang function:
weather_parser(new)

#can also just write as:
# weather_parser(args.location)