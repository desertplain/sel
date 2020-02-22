#python 2 + selenium

from selenium import webdriver
from time import sleep
import unittest


print 'hellou mai frend'

# tworzymy klase wspplcheck dziedziczaca po z modulu unittest

class WsbPlcheck(unittest.TestCase):
    """"scenariusz testowy"""
    # Warunki wstepne
    # Przygotowanie testow
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    #wlasciwe testy
    def testWsb(self):
        driver=self.driver
        driver.get('http://www.wsb.pl')
        self.assertIn('Bankowe',driver.title)
        print(driver.title)


    # sprztanie
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
