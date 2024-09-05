import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from cookie_timer import Timer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


def buy_improvements(event):
    while event.is_set():
        print("buy improvement")
        time.sleep(5)   # 5 seconds.


def click_cookie(event):
    while event.is_set():
        cookie.click()
        time.sleep(0.1)


improvements_timer = Timer(buy_improvements)

cookie = driver.find_element(By.ID, value="cookie")
click_cookie_timer = Timer(click_cookie)

# Wait 10 seconds and then stop the timer.
time.sleep(10)

improvements_timer.stop()
click_cookie_timer.stop()
driver.quit()
