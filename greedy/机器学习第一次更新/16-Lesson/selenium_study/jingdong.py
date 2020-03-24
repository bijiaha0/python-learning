import time
import os
from selenium.webdriver import ActionChains

__author__ = "zhou"
__date__ = "2019-05-30 20:37"

from selenium import webdriver

driver = webdriver.Chrome("/workspace/greedy_ai/python_and_ai/chromedriver")
driver.maximize_window()


def to_goods_page(driver):
    # 获取到京东首页
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_link_text("电脑")

    # 鼠标悬停
    ActionChains(driver).move_to_element(computer_element).perform()

    # 鼠标要点击一下笔记本
    time.sleep(5)
    driver.find_element_by_link_text("笔记本").click()

    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_window_handle
    for handle in handles:
        if handle != index_handle:
            # driver.close()
            driver.switch_to.window(handle)

    # 点击thinkpad
    driver.find_element_by_xpath("//*[@id=\"brand-11518\"]/a/img").click()
    # 点击7000以上
    driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div/div[2]/div/ul/li[7]/a').click()
    # 点击评论数
    driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[3]').click()
    # 点第一款电脑
    driver.find_element_by_xpath('//*[@id="plist"]/ul/li[1]/div/div[1]/a/img').click()

    # 切换句柄
    notebook_handler = driver.current_window_handle
    # 重新获取一下所有的句柄
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notebook_handler:
            driver.switch_to.window(handle)

    time.sleep(2)
    # 滚一下滚动条。 让大家能够看得见
    js = "window.scrollTo(0,1000)"
    driver.execute_script(js)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 定位到所有表格中的数据

    info_elements = driver.find_elements_by_class_name("Ptable-item")
    # 声明一个变量，用来装一下所有的结果数据
    result_list = []

    for info_element in info_elements:
        # 解析商品信息数据，获取一个字典格式的数据
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)

    # 信息保存到文件中
    save_goods_info(result_list)

def get_info_element_dict(info_element):
    # 计算机的组成信息，第一列信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机的key ，第二列的信息，就是那个dt
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # value， 第三列的信息
    computer_info_values = info_element.find_elements_by_xpath("dl//dd[not(contains(@class,'Ptable-tips'))]")

    # 声明一个空字典，来存储计算机信息中的key和value
    key_and_value_dict = {}

    # 声明一个空字典，用来存储计算机组成信息的字典
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text

    parts_dict[computer_part.text] = key_and_value_dict
    return parts_dict

def save_goods_info(result_list):
    # 声明一下要保存到哪个文件夹下
    project_path = os.path.abspath(os.path.curdir)
    print("project_path : " + project_path)

    file_path = project_path + "/goods_infos/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open(file_path + "computer.infos", 'a', encoding="utf-8") as f:
        f.write(str(result_list))
        print(str(result_list))



if __name__ == "__main__":
    to_goods_page(driver)



