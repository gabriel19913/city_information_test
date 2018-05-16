def formatted_city_country(city, country, population=''):
    '''This function formats the information that the user enters, if he/she type the population the information is displayed in a diffent way when he/she doesn't do it.'''
    if population:    
        formatted = city.title() + ', ' + country.title() + ' - population: ' + population + ' inhabitants.'
    else:
        formatted = city.title() + ', ' + country.title()
    return formatted
