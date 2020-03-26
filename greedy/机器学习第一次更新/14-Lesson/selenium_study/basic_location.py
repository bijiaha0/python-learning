from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time

driver = webdriver.Chrome("/workspace/greedy_ai/python_and_ai/chromedriver")
driver.get("https://www.jd.com")

search_element = driver.find_element_by_id("key")
search_element.send_keys("电脑")
search_element.send_keys(Keys.RETURN)

driver.find_element_by_class_name("cate_menu_lk").click()
driver.find_element_by_link_text("手机").click()
driver.find_element_by_partial_link_text("个护").click()
driver.find_element_by_xpath("//*[@id=\"J_cate\"]/ul/li[2]/a[2]").click()
driver.find_element_by_css_selector('#J_cate > ul > li:nth-child(4) > a:nth-child(7)').click()
# time.sleep(3)
# driver.quit()


