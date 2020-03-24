__author__ = "zhou"
__date__ = "2019-05-25 21:47"

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("/workspace/greedy_ai/python_and_ai/chromedriver")
driver.get("https://www.jd.com")

elem = driver.find_element_by_link_text("手机")
ActionChains(driver).move_to_element(elem).perform()

time.sleep(5)

old_phone = driver.find_element_by_link_text("老人机")
old_phone.click()







