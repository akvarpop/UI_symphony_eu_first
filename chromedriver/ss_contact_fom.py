import time

from selenium import webdriver
# options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# Disable webdriver mode(отображает нас как пользователя а не как вебдрайвер)
options.add_argument("--disable-blink-features=AutomationControlled")
# do not open in browser window(не открывать в окне браузера)
# options.add_argument("--headless")
# options.headless = True

# driver = webdriver.Chrome(executable_path='C:/Selenium_PythonToday/chromedriver/chromedriver.exe') (old code)
s = Service('C:/Selenium_PythonToday/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
# разделитель в отчете
separator = 20 * '-'

try:
    # Open page Contact Us
    print('Open site, symphony-solutions.eu On page contact-us\n', separator)
    driver.maximize_window()
    driver.get('https://www.symphony-solutions.eu/contact-us/')
    time.sleep(2)

    # cookies_I_Accept
    print('cookies_I_Accept\n', separator)
    driver.find_element(By.ID, 'cn-accept-cookie').click()

    # Enter in the field Name
    print('Enter in the field Name\n', separator)
    name_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[2]/input')
    name_input.clear()
    name_input.send_keys('test')

    # Enter in the field Email
    print('Enter in the field Email\n', separator)
    email_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[3]/input')
    email_input.clear()
    email_input.send_keys('test@test.test')

    # Enter in the field Massage
    print('Enter in the field Massage\n', separator)
    message_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[4]/textarea')
    message_input.clear()
    message_input.send_keys('test')

    # Click Privacy Policy
    print('Click Privacy Policy\n', separator)
    driver.find_element(By.XPATH,
                        '//*[@id="wpcf7-f10029-o1"]/form/span[5]/span/span/label/span').click()
    time.sleep(5)

    # Click Contact Us
    print('Click Contact Us\n', separator)
    driver.find_element(By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/input').click()
    time.sleep(3)

    # make screenshot
    print('make screenshot page\n', separator)
    driver.get_screenshot_as_file('contact_form.png')
    # driver.save_screenshot('2.png')
    print('Successfully')

except Exception as ex:
    print(ex)
finally:
    time.sleep(2)
    driver.close()
    driver.quit()
