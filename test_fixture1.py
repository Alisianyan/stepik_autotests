import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self):
        try:
            print(link)
            driver.get(link)
            assert(2 == 3), ""
#            browser.find_element_by_css_selector("#login_link")
        finally:
            driver.close()

    def test_guest_should_see_basket_link_on_the_main_page():
        driver.get(link)
        driver.find_element_by_css_selector(".basket-mini .btn-group > a")