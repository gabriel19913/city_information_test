import unittest
import city_function

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        '''Cities and countries as 'Santiago, Chile' work?'''
        formatted = city_function.formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')
    def test_city_country_population(self):
        '''Cities, countries and population as 'Santiago, Chile - population: 50000 inhabitants' work?'''
        formatted = city_function.formatted_city_country('santiago', 'chile', '50000')
        self.assertEqual(formatted, 'Santiago, Chile - population: 50000 inhabitants.')
if __name__ == '__main__':
    unittest.main()
