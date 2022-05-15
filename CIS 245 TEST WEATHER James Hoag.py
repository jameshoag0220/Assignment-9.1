# Python program to find current
# weather details of any city
# using openweathermap api
 
# import required modules
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)

 
# Ask for city name or zip code
city_name = input("Enter city name you would like the weather for, or Z for zip code: ")
if city_name == "z" || "Z":
    zip_code = input("Enter the zip code: ")
    complete_url = BASE_URL + "appid=" + api_key + "&q=" + zip_code
 
else:
    complete_url = BASE_URL + "appid=" + api_key + "&q=" + city_name

 

# return response object
response = requests.get(complete_url)
#convert to Python
x = response.json()
 

# "404" cod key means city is found 
if x["cod"] != "404":

    # print the temperature
    #need to create current_temperature variable??
    print(" Temperature: " + str(current_temperature)) 
 
else:
    print(" City Not Found ")
