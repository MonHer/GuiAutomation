# -*- coding: utf-8 -*-
# @Pjname ：GuiAutomation
# @Time   : 2020/06/06/19:03
# @Author : Yuye
# @File   : test_dome.py

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class Testweb(object):
    def setup(self):
        # options = webdriver.ChromeOptions()
        # options.headless = "true"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Remote(command_executor="127.0.0.1:4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX, proxy=None,)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test-web.xinkangzaixian.cn")

    def test_login(self):
        assert self.driver.find_element_by_xpath('//*[@placeholder="请输入账号"]')
        self.driver.find_element_by_xpath('//*[@placeholder="请输入账号"]').send_keys("qq")
        self.driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("123456")
        self.driver.find_element_by_xpath('//*[@type="button"]').click()

    def test_basc(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main("-s", "-v")