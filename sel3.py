#python 2 + selenium

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import unittest

email='llolla@op.pl'
birthday='3'
birthmonth='12'
birthyear='2000'
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
        sleep(5)
        email_input=driver.find_element_by_id('email_create')
        email_input.send_keys(email)
        create_btn=driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        sleep(5)

        account_name=driver.find_element_by_id('customer_firstname')
        account_name.send_keys('namecc')

        driver.find_element_by_id('id_gender1').click()

        account_last_name=driver.find_element_by_id('customer_lastname')
        account_last_name.send_keys('lasname')

        email_text=driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email

        passwd=driver.find_element_by_id('passwd')
        passwd.send_keys('haslo')



        day_of_birth_select=Select(driver.find_element_by_id('days'))
        day_of_birth_select.select_by_value(birthday)

        month_of_birth_select=Select(driver.find_element_by_id('months'))
        month_of_birth_select.select_by_value(birthmonth)

        year_of_birth_select=Select(driver.find_element_by_id('years'))
        year_of_birth_select.select_by_value(birthyear)


        sleep(10)
        #self.assertIn('Bankowe',driver.title)
        #print(driver.title)


    # sprztanie
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)



    """"

    """
