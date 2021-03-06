from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget

# get chrome web driver and open the insta link 
driver = webdriver.Chrome(r'C:\Users\bobo2\AppData\Local\Programs\Python\Python38\chromedriver.exe')
driver.get('https://www.instagram.com/')


# targeting username and password boxes

username = WebDriverWait(  driver , 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name = 'username']")))
password = WebDriverWait(  driver , 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name = 'password']")))

# clear the box in case the old login is saved 

username.clear()
password.clear()

username.send_keys('')
password.send_keys('')

log_in = WebDriverWait(  driver , 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "button[type = 'submit']"))).click()


# clicking not now when insta asks
not_now = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//button[contains(text() , 'Not Now')]"))).click()
# clicking the not now when insa asks to save log in info 
not_now2 = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//button[contains(text() , 'Not Now')]"))).click()

# search menu

searchbox = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//input[@placeholder = 'Search' ] ")))
searchbox.clear()
keyword = '#bikini'
searchbox.send_keys(keyword)
searchbox.send_keys(Keys.RETURN)   # problem here
searchbox.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0,4000);")

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path , keyword[1:] + "pics" )

os.mkdir(path)


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + ' .jjpg')
    wget.download(image, save_as)
    counter += 1
    







                                                    

                                                                           
                                                                           
                                                                           
