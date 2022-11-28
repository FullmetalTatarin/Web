from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:8000/')
driver.implicitly_wait(10)
sleep(1)
driver.find_element(By.LINK_TEXT, 'Логин').click()
driver.find_element(By.CLASS_NAME, 'login').send_keys("yaroslav")
driver.find_element(By.CLASS_NAME, 'password').send_keys("12345")
sleep(1)
driver.find_element(By.TAG_NAME, 'input').submit()
sleep(1)
driver.find_element(By.CLASS_NAME, 'search_by_city').send_keys('Москва')
sleep(1)
driver.find_elements(By.TAG_NAME, 'input')[1].submit()
sleep(1)
books = driver.find_elements(By.NAME, 'deleteBook')
books[0].click()
