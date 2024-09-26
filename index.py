import time
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



chromeOptins = webdriver.ChromeOptions()
# chromeOptins.add_argument("--headless")
# chromeOptins.page_load_strategy = "eager"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chromeOptins)

driver.get('https://www.shopmyexchange.com/register')

from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
import time

def run_selenium_thread(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Имитация работы с веб-страницей
    print(f"Opened {driver.title}")
    time.sleep(3)
    
    driver.quit()

# Список URL для открытия
urls = ["https://www.google.com", "https://www.python.org", "https://www.github.com"]

# Использование ThreadPoolExecutor для запуска потоков
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(run_selenium_thread, urls)

print("All threads finished.")

# firstName = driver.find_element("xpath", "//input[@name='firstName']")
# firstName.send_keys("jeffery")

# lastName = driver.find_element("xpath", "//input[@name='lastName']")
# lastName.send_keys("myer")

# ssn = driver.find_element("xpath", "//input[@name='ssn']")
# ssn.send_keys("0054")

# selectElementDay = driver.find_element("xpath", "//select[@name='dobDay']")
# selectDay = Select(selectElementDay)
# selectDay.select_by_value('06')

# selectElementMonth = driver.find_element("xpath", "//select[@name='dobMonth']")
# selectMonth = Select(selectElementMonth)
# selectMonth.select_by_value('12')

# selectElementYear = driver.find_element("xpath", "//select[@name='dobYear']")
# selectYear = Select(selectElementYear)
# selectYear.select_by_value('1960')

# email = driver.find_element("xpath", "//input[@name='email']")
# email.send_keys("sergio_omar831@yahoo.com")

# confirmEmail = driver.find_element("xpath", "//input[@name='confirmEmail']")
# confirmEmail.send_keys("sergio_omar831@yahoo.com")

# service = driver.find_element("xpath", "(//section[contains(@class, 'relative')])[17]")
# service.click()

# submit = driver.find_elements(By.CLASS_NAME, 'mt-6')[1]
# submit.click()


lines = []
with open('emails.txt', 'r') as file:
    lines = file.readlines()  

cok = driver.get_cookie("frontastic-session")

header = {
    'Frontastic-Session': cok['value']
}

for element in lines:
    data = {
        'email': element.replace("\n", "")
    }
    response = requests.post('https://service.shopmyexchange.com/frontastic/action/account/isEmailExist', headers=header, json=data)
    print(element ,response.json()['body'])


# time.sleep(10)