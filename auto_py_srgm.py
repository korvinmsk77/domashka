import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/py_8_10_drver_selenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#Open_site
driver.get("https://qa.neapro.site/login")
driver.set_window_size(930, 1060)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("srgm@yopmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("10101074")

driver.find_element(By.XPATH, "//a[contains(text(),'Забыли пароль?')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".fill").click() # witn xpath doesn't work
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(@href, '/login')]").click()

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("srgm@yopmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("10101074")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

#Fill_passport
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.XPATH, "//input[@id='surname']").send_keys("Скайвокер")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Люк")
driver.find_element(By.XPATH, "//input[@id='patronymic']").send_keys("Джедай")
driver.find_element(By.XPATH, "//input[@name='date']").click()
driver.find_element(By.XPATH, "//input[@name='date']").send_keys("19.04.1984")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='passportSeries']").click()
driver.find_element(By.XPATH, "//input[@id='passportSeries']").clear()
driver.find_element(By.XPATH, "//input[@id='passportSeries']").send_keys("5296")

driver.find_element(By.XPATH, "//input[@id='passportNumber']").click()
driver.find_element(By.XPATH, "//input[@id='passportNumber']").clear()
driver.find_element(By.XPATH, "//input[@id='passportNumber']").send_keys("145236")

driver.find_element(By.XPATH, "(//input[@name='date'])[2]").click()
driver.find_element(By.XPATH, "(//input[@name='date'])[2]").send_keys("26.08.2006")

driver.find_element(By.XPATH, "//input[@id='code']").click()
driver.find_element(By.XPATH, "//input[@id='code']").clear()
driver.find_element(By.XPATH, "//input[@id='code']").send_keys("523698")

driver.find_element(By.XPATH, "//input[@id='cardId']").click()
driver.find_element(By.XPATH, "//input[@id='cardId']").clear()
driver.find_element(By.XPATH, "//input[@id='cardId']").send_keys("14253698253")

driver.find_element(By.XPATH, "//input[@id='issued']").click()
driver.find_element(By.XPATH, "//input[@id='issued']").send_keys("Римским преториумом")

driver.execute_script("window.scrollTo(0, 500)")

driver.find_element(By.XPATH, "(//input[@type='text'])[7]").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[7]").send_keys("Запорожская обл, Запорожский р-н, г Запорожье, ул Вроцлавская")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()

driver.find_element(By.XPATH, "//input[@id='phone']").click()
driver.find_element(By.XPATH, "//input[@id='phone']").clear()
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("4125863967")

driver.find_element(By.XPATH, "//input[@id='privacy']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='privacy']").click()

#driver.find_element(By.XPATH, "//button[contains(.,'Прикрепить')]").click()
driver.find_element(By.XPATH, "//input[@type='file']").send_keys("C:\\Users\\esgre\\OneDrive\\Изображения\\bund-1.jpg")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 500)")

driver.find_element(By.XPATH, "//button[contains(.,'Отправить')]").click()