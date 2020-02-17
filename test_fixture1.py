from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

link = "http://selenium1py.pythonanywhere.com/"

#driver = WebDriver(executable_path='C:\Python33\chromedriver_win32\chromedriver')


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector("#login_link")

        def test_guest_should_see_basket_link_on_the_main_page(self):
            self.browser.get(link)
            self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")



    class TestMainPage2():

        def setup_method(self):
            print("start browser for test..")
            self.browser = webdriver.Chrome()

        def teardown_method(self):
            print("quit browser for test..")
            self.browser.quit()

        def test_guest_should_see_login_link(self):
            self.browser.get(link)
            self.browser.find_element_by_css_selector("#login_link")

        def test_guest_should_see_basket_link_on_the_main_page(self):
            self.browser.get(link)
            self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
