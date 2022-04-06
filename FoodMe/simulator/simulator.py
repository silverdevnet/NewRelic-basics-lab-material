import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
url = "http://localhost:3000/#/customer"
restaurants = [
    "robatayaki",
    "sallys",
    "speisewagen",
    "beijing",
    "curryup",
    "babythai",
    "pedros",
    "thick",
]
name = [
    "Joe Black",
    "James",
    "Robert",
    "Patricia",
    "Rebecca",
    "Linda",
]

while True:
    browser.get(url)
    time.sleep(1)

    customer_name = browser.find_element(By.ID, "customerName")
    customer_name.clear()
    customer_name.send_keys(random.choice(name))
    time.sleep(1)

    address = browser.find_element(By.ID, "address")
    address.clear()
    address .send_keys("432 Wiggly Rd, Mountain View, 94043")
    time.sleep(1)

    browser.find_element(By.ID, "restaurants").click()

    restaurant = random.choice(restaurants)
    browser.get(f"http://localhost:3000/#/menu/{restaurant}")
    time.sleep(2)

    menu = browser.find_element(By.ID, "menu")
    items = menu.find_elements(By.ID, "menuItem")
    order_items = random.sample(items, 3)

    for o in order_items:
        Hover = ActionChains(browser).move_to_element(o)
        Hover.click().perform()
        time.sleep(1)

    browser.find_element(By.LINK_TEXT, "Checkout").click()
    time.sleep(2)

    payment = Select(browser.find_element(By.TAG_NAME, "select"))
    payment.select_by_index(random.randrange(1, 4))
    card = payment.first_selected_option
    time.sleep(2)

    credit_card_number = browser.find_element(By.NAME, "ccNum")
    credit_card_number.clear()

    num = ''.join(random.choice(string.digits) for _ in range(16))
    credit_card_number.send_keys(num)
    time.sleep(1)

    browser.find_element(By.NAME, "ccExp").clear()
    browser.find_element(By.NAME, "ccExp").send_keys("05/2025")
    time.sleep(1)

    cvc = ''.join(random.choice(string.digits) for _ in range(3))
    credit_card_cvc = browser.find_element(By.NAME, "ccCvc")
    credit_card_cvc.clear()
    credit_card_cvc.send_keys(cvc)
    time.sleep(2)

    xpath = '//button[text()="Purchase"]'
    browser.find_element(By.XPATH, xpath).click()
    time.sleep(5)
