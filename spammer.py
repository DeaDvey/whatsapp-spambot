#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import xlsxwriter
import pathlib
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


#defines relevant driver options
opts = ChromeOptions()#defines the options
opts.add_argument("--window-size=1500,1500")#defines window size
#opts.add_argument("--headless") #uncomment this if you don't want to see window, wont work on whatsapp as you need to verify the QR code
driver_path = (pathlib.Path(__file__).parent / 'chromedriver').resolve()#find crome driver
driver = webdriver.Chrome(str(driver_path), options=opts)
driver.implicitly_wait(5) # Just in case the page takes a while to load

#go to whatsapp website
driver.get("https://web.whatsapp.com")

input()#waits until return key hit
print("spamming")#tells ou the program has begun
text_field = driver.find_element(By.CSS_SELECTOR, "._3Uu1_ .to2l77zo")#defines text box
counter = 0#defines counter

while 1 == 1:#repeats forever
    counter+=1#increment counter
    time.sleep(0.4)#sleeps for a bit to prevent it bullying my cpu
    text_field.send_keys(counter)#prints the phrase into the textbox
    send_button = driver.find_element(By.CSS_SELECTOR, "._2xy_p  .tvf2evcx")#finds send button
    send_button.click()#clicks send button


driver.quit()



