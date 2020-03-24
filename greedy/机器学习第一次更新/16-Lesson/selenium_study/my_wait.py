__author__ = "zhou"
__date__ = "2019-05-30 21:56"

from selenium import webdriver
driver = webdriver.Chrome("/workspace/greedy_ai/python_and_ai/chromedriver")
driver.maximize_window()


#强制等待  .  time.sleep(10)
# 隐性等待
# driver.implicitly_wait(10)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 首先要说明一下等待的条件
driver.get("https://list.jd.com/list.html?cat=670,671,672")
locator = (By.CSS_SELECTOR, "#plist > ul > li:nth-child(1) > div > div.p-img > a > img")
element = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
element.click()









