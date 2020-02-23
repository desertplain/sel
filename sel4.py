#python 2 + selenium

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import unittest

email='llolla@op.pl'
fname='misiek'
lname='misiowy'
haslo='haslo'
birthday='3'
birthmonth='12'
birthyear='2000'
adres='radosna 1'
miasto='wroclaw'
stan='Alabama'
kod='55-555'
kraj='United States'
fon='121212121'
aliasss='buda'

print 'hellou mai frend'

# tworzymy klase wspplcheck dziedziczaca po z modulu unittest

class APRegistration(unittest.TestCase):
    """"scenariusz testowy"""
    # Warunki wstepne
    # Przygotowanie testow
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://automationpractice.com')
        self.driver.implicitly_wait(10)
    #wlasciwe testy
    def testCorrectRegitration(self):
        #odnajdz i kliknij sign in ,
        driver=self.driver
        driver.find_element_by_class_name('login').click()

        driver.find_element_by_id('email_create').send_keys(email)

        driver.find_element_by_id('SubmitCreate').click()

        driver.find_element_by_id('customer_firstname').send_keys(fname)

        driver.find_element_by_id('id_gender1').click()

        driver.find_element_by_id('customer_lastname').send_keys(lname)

        driver.find_element_by_id('passwd').send_keys(haslo)

        Select(driver.find_element_by_id('days')).select_by_value(birthday)

        Select(driver.find_element_by_id('months')).select_by_value(birthmonth)

        Select(driver.find_element_by_id('years')).select_by_value(birthyear)

        email_text=driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email
        print email_text

        fname_text=driver.find_element_by_id('firstname').get_attribute('value')
        assert fname_text == fname
        print fname_text

        lname_text=driver.find_element_by_id('lastname').get_attribute('value')
        assert lname_text == lname
        print lname_text

        driver.find_element_by_id('address1').send_keys(adres)

        driver.find_element_by_id('city').send_keys(miasto)

        driver.find_element_by_id('id_state').send_keys(stan)

        driver.find_element_by_id('postcode').send_keys(kod)

        driver.find_element_by_id('id_country').send_keys(kraj)

        driver.find_element_by_id('phone_mobile').send_keys(fon)

        driver.find_element_by_id('alias').clear()
        driver.find_element_by_id('alias').send_keys(aliasss)
    
        driver.find_element_by_id('submitAccount').click()

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
