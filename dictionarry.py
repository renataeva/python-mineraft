from pprint import pp
weather = {
    'temp': 20,
    'windspeed': 5,
    'precipitation': None,
    'pressure': 625
}
print(type(weather))
print(weather)
pp(weather, width=15)
pp(list(weather.values()), width=2)
