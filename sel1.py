#python 2 + selenium



from selenium import webdriver
from time import sleep

print 'hellou mai frend'

#tworzymy obiekt klasy webdriver
driver = webdriver.Firefox()
driver.get('http://www.google.com')
driver.maximize_window()
#spij 5s
sleep(5)
driver.quit()
