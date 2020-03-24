from config import basic_settings

__author__ = "zhou"
__date__ = "2019-06-01 22:09"

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url


    def open(self):
        self._driver.get(url=self._url)
        return self._driver

    def find_element(self, *locator, element=None, timeout=None, wait_type="visibility"):

        if element is not None:
            return self._init_wait(timeout).until(EC.visibility_of(element.find_element(*locator)))

        if wait_type == "visibility":
            return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
        else:
            return self._init_wait(timeout).until(EC.presence_of_element_located(locator=locator))



    def send_keys(self, web_element, keys):
        web_element.clear()
        web_element.send_keys(keys)



    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=basic_settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
