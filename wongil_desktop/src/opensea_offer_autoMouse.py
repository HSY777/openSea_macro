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
    url = 'https://opensea.io/assets/klaytn/0xce8905b85119928e6c828e5cb4e2a9fd2e128bf9/'
    for i in range(6276, 9001):  #5650 까지 했음(주계정)
        delay = 3.5
        margin = 345
        # a, b = pyautogui.size()  # 해상도 반환
        a, b = pyautogui.position()   # 마우스 좌표 반환
        print(a, b)
        pyautogui.moveTo(1526, 526, 0.1) # 마우스 움직임
        pyautogui.click(x = margin + 1526, y = 526) # 일단클릭
        pyautogui.click(x = margin + 1245, y = 60)   # url 네비게이터 클릭
        pyautogui.typewrite(url + str(i))
        pyautogui.press('enter') # url 입력
        time.sleep(5)
        pyautogui.click(x = margin + 927, y = 382) # make offer 클릭
        time.sleep(delay)
        pyautogui.click(x = margin + 663, y = 603) # 체크박스 클릭
        time.sleep(delay)
        pyautogui.click(x = margin + 833, y = 327)  # wkly 입력창 클릭
        pyautogui.typewrite('30')
        time.sleep(1)
        pyautogui.click(x = 1025, y = 411) # 날짜 클릭
        time.sleep(1)
        pyautogui.click(x = 1025, y = 530) # 30일 클릭
        time.sleep(1)
        pyautogui.click(x = margin + 800, y = 513) # make offer 클릭(결제창)
        time.sleep(delay)
        pyautogui.click(x = margin + 651, y = 439)  # 사인 클릭


        time.sleep(delay)
        # pyautogui.moveTo(233, 564, 0.1) # 마우스 움직임
        pyautogui.click(x = 233, y = 564)  # 카이카스 서명 클릭
        time.sleep(delay)



if __name__ == '__main__':
    main()