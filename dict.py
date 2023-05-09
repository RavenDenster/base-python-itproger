country = {
    (5,6): 3,
}
print(country[5,6])

country = {
    'code': 'Ru',
    'name': 'Russian',
    'population': 144
}

print(country.keys(), country.values())

for key, value in country.items():
    print(key, ' - ', value)

print(country['code'])
print(country.get('code'))

country.pop('name')
country.popitem()
print(country)