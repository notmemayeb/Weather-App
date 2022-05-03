import requests 
import PySimpleGUI as sg
from secrets import key


layout = [
	[sg.Text('Type city name: ', key = '-TITTLE-')],
	[sg.Input(key = '-INPUT-'), sg.Button('Search', key = '-SEARCH-')],
	[sg.Text('', key = '-OUTPUT-')]
]

window = sg.Window('Not my Weather App' , layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		print('Goodbye!')
		break
	if event == '-SEARCH-':
		city = values['-INPUT-']
		r = requests.get(
			'https://api.openweathermap.org/data/2.5/weather?',
			params = {'q': city, 'appid': key, 'units': 'metric'
		})
		data = r.json()
		if data['cod'] == 200:
			weather = data['weather'][0]['description']
			temp = data['main']['temp']
			output = f'Today the weather in {city} is {weather}! Its {temp} degrees'
		elif data['message'] == 'city not found':
			output = 'Incorrect city name!'
		else:
			output = 'Error!'

		window['-OUTPUT-'].update(output)

window.close()
