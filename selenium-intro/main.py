from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

events_widget = driver.find_element(By.CSS_SELECTOR, value=".event-widget ul")
events = events_widget.find_elements(By.TAG_NAME, value="li")

events_dict = {}
for i, event in enumerate(events):
    time = event.find_element(By.TAG_NAME, value="time")
    name = event.find_element(By.TAG_NAME, value="a")
    events_dict[i] = {time.text: name.text}

print(events_dict)

# Closes all tabs and browser
driver.quit()
