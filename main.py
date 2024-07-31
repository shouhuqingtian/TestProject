from utils.screenshot import Screenshot
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    capture_unit = Screenshot(driver, "http://192.168.16.50:10006/login", 10)
    capture_unit.capture_and_crop("#app > div.login-container > form > div.login-container-code > div.login-container-codeImg > img", "../picture/captcha.png")
