from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver_option = input("'chrome'/'c' or 'firefox'/'f'? ")

if driver_option.lower() == ("f" or "firefox"):
    # set the path to the geckodriver executable
    gecko_path = './geckodriver'

    # set the Firefox profile options (optional)
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.cache.disk.enable', False)

    # create the webdriver instance using geckodriver
    driver = webdriver.Firefox(executable_path=gecko_path, firefox_profile=profile)

elif driver_option.lower() == ("c" or "chrome"):
    chrome_path = './chromedriver'
    options = ChromeOptions()
    driver = Chrome(executable_path=chrome_path, options=options)


# navigate to a website
driver.get('https://web.whatsapp.com')

spam_phrase = input("Enter the spam phrase ('counter' for an infinite counter): ")
#spam_phrase = input()
print(spam_phrase)


input("When you are on the selected chat hit enter ")
print("spamming")#tells ou the program has begun
text_field = driver.find_element(By.CSS_SELECTOR, "._3Uu1_ .to2l77zo")#defines text box
counter = 0#defines counter


if spam_phrase.lower() == "counter":
    while 1 == 1:#repeats forever
        counter+=1#increment counter
        time.sleep(0.4)#sleeps for a bit to prevent it bullying my cpu
        text_field.send_keys(counter)#prints the phrase into the textbox
        driver.find_element(By.CSS_SELECTOR, "._2xy_p  .tvf2evcx").click()

elif spam_phrase.lower() != "counter":
    while 1 == 1:#repeats forever
        time.sleep(0.1)#sleeps for a bit to prevent it bullying my cpu
        for char in spam_phrase:
            text_field.send_keys(char)#prints the phrase into the textbox
        driver.find_element(By.CSS_SELECTOR, "._2xy_p  .tvf2evcx").click()



time.sleep()
# close the webdriver instance
driver.quit()
