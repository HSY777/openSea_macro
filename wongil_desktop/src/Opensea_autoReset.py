import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import threading, queue, time

        

def main():

    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url='https://opensea.io/collection/treasures-club-masters?search[sortAscending]=false&search[sortBy]=LISTING_DATE')


    time.sleep(10)
    # element = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div/div/div[3]/div[1]/div[1]/input')
    
    while True:
        time.sleep(10)
        driver.refresh()
        print(1)
        # element.send_keys(Keys.ENTER)

    

if __name__ == '__main__':
    main()




