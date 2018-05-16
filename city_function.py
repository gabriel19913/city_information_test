def formatted_city_country(city, country):
        formatted = city.title() + ', ' + country.title()
        print('\n------------------------------------------------------')
        print(formatted)            
        print('------------------------------------------------------')

def get_city_info_loop():
    print('\n------------------------------------------------------')
    print('Type "q" if you want to quit at any moment.')
    while True:
        city = input('\nWhat is the city name? ')
        if city == 'q':
                break
        country = input('What is the country name? ')
        if country == 'q':
            break
        else:
            formatted_city_country(city, country)

get_city_info_loop()