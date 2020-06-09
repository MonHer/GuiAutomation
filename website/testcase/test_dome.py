# -*- coding: utf-8 -*-
# @Pjname ：GuiAutomation
# @Time   : 2020/06/06/19:03
# @Author : Yuye
# @File   : test_dome.py

import pytest
from selenium import webdriver


class Testweb(object):
    def setup(self):
        # self.driver = webdriver.Firefox()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://test-web.xinkangzaixian.cn")
        self.driver.maximize_window()
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(30)

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
    pytest.main()