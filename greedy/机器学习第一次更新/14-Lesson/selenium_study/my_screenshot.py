__author__ = "zhou"
__date__ = "2019-05-25 21:58"


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


# 获取当前窗口中的所有句柄 ，这里获取到的句柄数量就是两个
handles = driver.window_handles
#  获取当前窗口的句柄，这里获取到的句柄数量就是一个
current_handle = driver.current_window_handle

# 句柄切换
for handle in handles:
    if handle != current_handle:
        driver.close()  # 关闭当前浏览器句柄
        # driver.quit()  # 关闭整个浏览器
        driver.switch_to.window(handle)
        # driver.save_screenshot("laorenji.jpg")
        driver.save_screenshot("laorenji.png")







