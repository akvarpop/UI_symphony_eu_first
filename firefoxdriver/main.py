from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = 'http://symphony-solutions.com/'
# driver = webdriver.Chrome(executable_path='C:/Selenium_PythonToday/chromedriver/chromedriver.exe') старый код
s = Service('C:/Selenium_PythonToday/firefoxdriver/geckodriver.exe')
driver = webdriver.Firefox(service=s)

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
