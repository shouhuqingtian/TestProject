import re
from playwright.sync_api import Page, expect, sync_playwright


'''def test_example():
    # 启动浏览器
    with sync_playwright() as p:
        # 启动浏览器，以可见模式（headless=False）
        browser = p.chromium.launch()
        page = browser.new_page()

        # 访问登录页面
        page.goto("http://192.168.16.50:10006/login?redirect=%2Fcustomer%2FinquiryBox%2FcustomerManage%3Ftype%3Dnav")

        page.get_by_placeholder("Username").click()
        page.get_by_placeholder("Username").fill("dev")
        page.get_by_placeholder("Password").click()
        page.get_by_placeholder("Password").fill("air2021")
        page.get_by_placeholder("验证码").click()
        page.get_by_placeholder("验证码").fill("5y65")
        page.get_by_role("button", name="Login").click()
        page.get_by_role("link", name="最低库存量").click()
        page.get_by_role("link", name="客户管理").click()
        page.get_by_role("button", name=" 新增客户").click()
        page.locator("div").filter(has_text=re.compile(r"^（注：编号必须是0001-2999的四位数字）$")).get_by_role("textbox").click()
        page.locator("div").filter(has_text=re.compile(r"^（注：编号必须是0001-2999的四位数字）$")).get_by_role("textbox").fill("001")
        page.get_by_placeholder("请选择拥有人").click()
        page.locator("li").filter(has_text="alex").nth(1).click()
        page.locator(".el-col > .el-form-item > .el-form-item__content > .el-input > .el-input__inner").first.click()
        page.locator(".el-col > .el-form-item > .el-form-item__content > .el-input > .el-input__inner").first.fill("0011")
        page.get_by_placeholder("请选择", exact=True).nth(2).click()
        page.locator("li").filter(has_text="是").nth(3).click()
        page.get_by_role("button", name="确 定").click()
        page.get_by_placeholder("请选择", exact=True).nth(4).click()
        page.locator("li").filter(has_text="中国(China)").nth(1).click()
        page.get_by_role("button", name="确 定").click()
        page.get_by_text("新增客户批量导入导出客户类型审批参数设置").click()
'''
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.get_by_role("link", name="飞机租赁管理").click()
    page.get_by_role("button", name=" 新增").click()
    page.locator(".w-250 > .el-input__inner").first.click()
    page.locator(".w-250 > .el-input__inner").first.fill("TEST")
    page.get_by_role("spinbutton").nth(1).click()
    page.get_by_role("spinbutton").nth(1).fill("1")
    page.get_by_role("tab", name="选择库存").click()
    page.get_by_role("button", name="选择库存").first.click()
    page.get_by_role("row", name="129319 航润 CFM56-7B26/3 --").locator("label span").nth(1).click()
    page.get_by_role("row", name="129018 航润 34600017 27759F1").locator("label span").nth(1).click()
    page.get_by_role("button", name="选择库存").nth(2).click()
    page.get_by_role("row", name="129406 航润 CFM56-5A3 -- V88889").locator("label span").nth(1).click()
    page.get_by_role("button", name="选择库存").nth(3).click()
    page.get_by_role("row", name="127534 航润 V2527-A5 -- V15988").locator("label span").nth(1).click()
    page.get_by_role("button", name="保 存").click()
    page.locator("div:nth-child(8) > .el-form-item > .el-form-item__content > .flex-center-start > div > .el-input > .el-input__inner").first.click()
    page.locator("li").filter(has_text="广州航润航空技术有限公司").locator("span").click()
    page.get_by_role("button", name="保 存").click()
    page.get_by_role("button", name="选择库存").nth(4).click()
    page.get_by_role("row", name="129306 航润 131 - 33645 -- AR").locator("label span").nth(1).click()
    page.get_by_role("button", name="保 存").click()
