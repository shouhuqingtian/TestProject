# -*- coding: utf-8 -*-
# @Time    : 2024/7/30
# @Author  : Bin
# @Software: PyCharm
# @File    : screenshot.py

from  selenium import webdriver
from PIL import Image
from io import BytesIO


class Screenshot:
    def __init__(self, driver: webdriver, url: str, timeout: int):
        self.driver = driver
        self.url = url
        self.timeout = timeout

    def capture_and_crop(self, element_selector: str, output_path: str):
        # 定位验证码元素
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)
        captcha_element = self.driver.findelement_by_css_selector(element_selector)

        #获取元素位置和大小
        location = captcha_element.location
        size = captcha_element.size
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']

        # 获取整个屏幕截图
        screenshot = self.driver.get_screenshot_as_png()

        # 使用PIL处理截图
        image = Image.open(BytesIO(screenshot))

        # 裁剪验证码图片
        captcha_image = image.crop((left, top, right, bottom))
        # 保存裁剪后的图像
        captcha_image.save(output_path)



