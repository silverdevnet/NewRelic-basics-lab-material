import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "http://localhost:3000/#/customer"
restaurants = ["robatayaki", "sallys", "speisewagen", "beijing", "curryup", "babythai", "pedros", "thick"]
name = ["Joe Black", "James", "Robert", "Patricia", "Rebecca", "Linda"]

while True:
    browser.get(url)
    time.sleep(1)
    address="432 Wiggly Rd, Mountain View, 94043"
    clear_name = browser.find_element(By.ID, "customerName").clear()
    name_text_field=browser.find_element(By.ID, "customerName").send_keys(random.choice(name))
    time.sleep(1)
    clear_address = browser.find_element(By.ID, "address").clear()
    address_text_field=browser.find_element(By.ID, "address").send_keys(address)
    time.sleep(1)

    button=browser.find_element(By.ID, "restaurants").click()
    time.sleep(2)

    restaurant = random.choice(restaurants)
    browser.get("http://localhost:3000/#/menu/" + restaurant)
    time.sleep(2)

    menu = browser.find_element(By.ID, "menu")
    items = menu.find_elements(By.ID, "menuItem")

    orderItem = random.sample(items,3)

    for o in orderItem:
        Hover = ActionChains(browser).move_to_element(o)
        Hover.click().perform()
        time.sleep(1)
    checkout = browser.find_element(By.LINK_TEXT, "Checkout").click()
    time.sleep(2)


    payment = Select(browser.find_element(By.TAG_NAME, "select"))
    payment.select_by_index(random.randrange(1,4))
    time.sleep(2)

    card = payment.first_selected_option

    clear_cardNum = browser.find_element(By.NAME, "ccNum").clear()

    num = ''
    for i in range(16):
        num = num + str(random.randint(0,9))
    cardNum = browser.find_element(By.NAME, "ccNum").send_keys(num)
    time.sleep(1)

    clear_cardExp = browser.find_element(By.NAME, "ccExp").clear()

    cardExp = browser.find_element(By.NAME, "ccExp").send_keys('05/2025')
    time.sleep(1)
    
    clear_cardCvc = browser.find_element(By.NAME, "ccCvc").clear()

    cvc = ''
    for i in range(3):
        cvc = cvc + str(random.randint(0,9))
    cardCvc = browser.find_element(By.NAME, "ccCvc")
    cardCvc.send_keys(cvc)
    time.sleep(2)

    purchase = browser.find_element(By.XPATH, '//button[text()="Purchase"]').click()
    time.sleep(5)
