# -*- coding: utf-8 -*-
# @Pjname ：GuiAutomation
# @Time   : 2020/06/09/21:37
# @Author : Yuye
# @File   : test_Yinuo.py

import json
import pytest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestYinuo(object):
    def setup_method(self):
        # self.driver = webdriver.Firefox()

        # options = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Remote(command_executor="127.0.0.1:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME, proxy=None)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test-web.xinkangzaixian.cn")

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        assert self.driver.find_element_by_xpath('//*[@placeholder="请输入账号"]')
        self.driver.find_element_by_xpath('//*[@placeholder="请输入账号"]').send_keys("qq")
        self.driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("123456")
        self.driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys(5555)
        self.driver.find_element_by_xpath('//*[@type="button"]').click()

    def test_execute_acript(self):
        rew = self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(json.dumps(json.loads(rew), indent=4))

if __name__ == "__main__":
    pytest.main()

