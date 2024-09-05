import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from cookie_timer import Timer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


def _extract_price(element):
    return int(element.find_element(By.TAG_NAME, value="b").text.split("-")[1].strip())


def _get_improvement(element_name):
    price = -1
    element = driver.find_element(By.ID, value=element_name)
    if element.get_attribute("class") != "grayed":
        price = _extract_price(element)

    return element, price


def _get_biggest_improvement(improvements_list):
    biggest_improvement = None
    for imp in improvements_list:
        if biggest_improvement is None or imp[1] > biggest_improvement[1]:
            biggest_improvement = imp

    return biggest_improvement[0]


def buy_improvements(event):
    while event.is_set():
        buy_cursor = _get_improvement("buyCursor")
        buy_grandma = _get_improvement("buyGrandma")

        improvements = [buy_cursor, buy_grandma]
        improvement_to_buy = _get_biggest_improvement(improvements)
        if improvement_to_buy is not None:
            print(f"Buying {improvement_to_buy.text}")
            improvement_to_buy.click()

        time.sleep(5)   # 5 seconds.


def click_cookie(event):
    while event.is_set():
        cookie.click()
        time.sleep(0.1)


improvements_timer = Timer(buy_improvements)

cookie = driver.find_element(By.ID, value="cookie")
click_cookie_timer = Timer(click_cookie)

# Wait 10 seconds and then stop the timer.
time.sleep(100)

improvements_timer.stop()
click_cookie_timer.stop()
driver.quit()
