#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/24 19:02
# @Author  : 习惯
# @File    : test_ui.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://erp.lemfix.com/login.html')
driver.find_element(By.ID, "username").click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('13916686542')
driver.save_screenshot('2.jpg')
time.sleep(1)
driver.close()
