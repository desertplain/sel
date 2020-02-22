#python 2 + selenium

from selenium import webdriver
from time import sleep
import unittest

email='lololla@op.pl'

print 'hellou mai frend'

# tworzymy klase wspplcheck dziedziczaca po z modulu unittest

class APRegistration(unittest.TestCase):
    """"scenariusz testowy"""
    # Warunki wstepne
    # Przygotowanie testow
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://automationpractice.com')
        #self.driver.maximize_window()

    #wlasciwe testy
    def testCorrectRegitration(self):
        #odnajdz i kliknij sign in ,
        driver=self.driver
        sign_in=driver.find_element_by_class_name('login')
        sign_in.click()
        email_input=driver.find_element_by_id('email_create')
        email_input.send_keys(email)
        create_btn=driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        account_name=driver.find_element_by_id('customer_firstname').click()
        account_name.send_keys('name')
        sleep(5)
        #self.assertIn('Bankowe',driver.title)
        #print(driver.title)


    # sprztanie
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)



    """"

    """
