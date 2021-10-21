import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import threading, queue, time

#url_list = ['%231111', '%232222', '%233333', '%234444', '%235555']
url_list = ['16374', '16339', '16341', '16340', '16370', '16372', '16371', '16373', '16361', '16368', '16363', '16364', '16365', '16366', '16367']
url_list = ['16368', '16369', '16375', '16376', '16377', '16378', '16379', '16380', '16381', '16382', '16383', '16384', '16342', '16343', '16344']
url_list = ['16345', '16346', '16347', '16348', '16349', '16350', '16351', '16352', '16353', '16354', '16355', '16356', '16357', '16358', '16359', '16360']


class Worker(threading.Thread):
    def __init__(self, url, num):
        super().__init__()
        self.url = url
        self.num = num
    
    def run(self):
        driver = webdriver.Chrome(executable_path='chromedriver')
        #driver.get(url='https://opensea.io/collection/dogesoundclub-mates?search[query]=' + url_list[self.num] + '&search[sortAscending]=true&search[sortBy]=PRICE')
        driver.get(url='https://opensea.io/assets/klaytn/0x4007cb1fb9d1158add29cf5d88568dd44a1f516e/' + url_list[self.num])
        # 바이나우 && 가격 있으면 값 가져오기
        time.sleep(100)

def startMor():
    create_url_thread = []
    print('asdf')
    for i in range(15):
        num = i
        create_url_thread.append(Worker(url_list[i], num))
    
    for i in range(15):
        create_url_thread[i].start()
        

def main():

    # for i in url_list:
    #     driver.get(url='https://opensea.io/collection/dogesoundclub-mates?search[query]=' + url_list[i] + '&search[sortAscending]=true&search[sortBy]=PRICE')

    #driver.get(url='https://opensea.io/collection/dogesoundclub-mates?search[query]=' + url_list[0] + '&search[sortAscending]=true&search[sortBy]=PRICE')

    t = threading.Thread(target = startMor)
    t.start()
    

if __name__ == '__main__':
    main()







