'''This is the main function, it calls the function formatted_city_country() to display a formatted information with what he/she typed.'''

from city_function import formatted_city_country
print('\n------------------------------------------------------')
print('Type "q" if you want to quit at any moment.')
# This while loop keeps asking for information and displaying the results 
# until the user enter the letter 'q'
while True:
    city = input('\nWhat is the city name? ')
    if city == 'q':
        break
    country = input('What is the country name? ')
    if country == 'q':
        break
    population = input('What is the city population? ')
    if population == 'q':
        break
    else:
        formatted = formatted_city_country(city, country, population)
    print('\n' + formatted)
    print('------------------------------------------------------')