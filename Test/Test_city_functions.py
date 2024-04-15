from city_functions import country_n_city
import unittest

class testcity_functions(unittest.TestCase):
    def test_is_equal(self):
        example = country_n_city('china','shanghai',population = '3000')
        output = 'Shanghai,China - population 3000'
        self.assertEqual(output,example)


if __name__ == '__main__':
    unittest.main()