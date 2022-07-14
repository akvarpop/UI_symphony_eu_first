from selenium import webdriver
import time

# options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# do not open in browser window(не открывать в окне браузера)
# options.add_argument("--headless")
# options.headless = True

s = Service('C:/Selenium_PythonToday/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

try:
    # Open main
    driver.maximize_window()
    driver.get('https://www.symphony-solutions.eu/')
    time.sleep(2)

    # Go to the page JoinUs
    joinus = driver.find_element(By.XPATH, '//*[@id="menu-item-7033"]/a').click()

    # click Quick Apply and go to the page quick-apply
    quickaplly = driver.find_element(By.XPATH, '//*[@id="filterForm"]/div[4]/p/a').click()

    # cookies_I_Accept
    driver.find_element(By.ID, 'cn-accept-cookie').click()

    # enter fields
    # Location - not required
    # Tehnology - not required

    # Enter text in the field Your Name
    your_name = driver.find_element(By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[3]/input')
    your_name.clear()
    your_name.send_keys('test')

    # Enter text in the field Your Email
    your_email = driver.find_element(By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[4]/input')
    your_email.clear()
    your_email.send_keys('test@test.test')

    # Upload CV
    driver.find_element(By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/div[2]/span[1]/input').send_keys(
        "C:/Selenium_PythonToday/chromedriver/test.pdf")
    time.sleep(3)
    # Click Private_Policy_1
    driver.find_element(By.XPATH, "//div[@id='wpcf7-f12314-p12310-o1']/form/span[5]/span/span/label/span").click()
    time.sleep(3)
    # Click Private_Policy_2
    driver.find_element(By.XPATH, "//div[@id='wpcf7-f12314-p12310-o1']/form/span[6]/span/span/label/span").click()
    time.sleep(3)

    # Clich Submit
    submit = driver.find_element(By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/input').click()
    time.sleep(5)

    # make screenshot
    driver.find_element(By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/div[5]')
    driver.get_screenshot_as_file('Join_Us.png')
    driver.save_screenshot('2.png')

except Exception as ex:
    print(ex)
finally:
    time.sleep(5)
    driver.close()
    driver.quit()