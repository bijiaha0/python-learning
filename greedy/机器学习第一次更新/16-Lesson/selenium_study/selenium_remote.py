
# 证明两个ip地址是通的，用ping idaddress
# 证明请求地址中的端口号是通的，用telnet ip port

data = {
    "linux": "http://localhost:4444/wd/hub",
    # "windows": "http://192.168.1.35:4444/wd/hub",
    # "linux2": "http://192.168.1.35:4444/wd/hub"
}

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

def to_baidu(name, address):
    print(name + "启动啦")
    driver = webdriver.Remote(
        command_executor=address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("https://www.baidu.com")

for name,url in data.items():
    print(url)
    t = Thread(target=to_baidu, args=(name,url))
    t.start()