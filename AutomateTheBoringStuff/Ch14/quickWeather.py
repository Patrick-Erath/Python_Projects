# quickWeather.py : Prints the weather for a location inputted in command line
import json, requests, sys

if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:]) # join all input strings

#f4df68bff742da1651e2601ddf40582e
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=919523ea10e7ffa0a3272ac075e69c02' %(location) #pass location into %s
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
print('Current weather in %s:' %(location))
print(weatherData['weather'][0]['main'], ' - ', weatherData['weather'][0]['description'])
minTemp = str(round(weatherData['main']['temp_min']-273))
maxTemp = str(round(weatherData['main']['temp_max']-273))
printThis = 'The temperature will be a minimum of %s and a maximum of %s Celcius' %(minTemp, maxTemp)
print(printThis)