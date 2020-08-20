import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

while True:
 
    chromeOptions = webdriver.ChromeOptions()
     
    browser = webdriver.Chrome('C:\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe', options=chromeOptions) #浏览器驱动
     
    browser.delete_all_cookies()  # 删除cookie
     
     
    browser.get("https://www.bilibili.com/video/av00000002") #视频地址
     
    element = WebDriverWait(browser, 15).until( #等待播放按钮能够被加载并且能够被点击，15s后如果还没加载完成并且不满足被点击的条件，就抛出异常
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[8]/video'))
    )
    element.click()
    print(browser.get_cookies())
    time.sleep(100)# 等待时常
    browser.quit()
