import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import threading, queue, time

import pyautogui        

def main():
    while True:
        # a, b = pyautogui.size()  # 해상도 반환
        a, b = pyautogui.position()   # 마우스 좌표 반환
        print(a, b)


if __name__ == '__main__':
    main()