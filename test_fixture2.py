"""Урок 3.4. и 3.5  Использование фикстур и Маркировка"""


import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def driver():
    print("\nstart browser for test..")
    driver = WebDriver(executable_path='C:\Python33\chromedriver_win32\chromedriver')
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр driver
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector("#login_link")

    # Добавляем маркер pytest.mark.regression
    @pytest.mark.skip
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector("input.btn.btn-default")




"""
запуск тестов с маркерами @pytest.mark.smoke и @pytest.mark.win10       -           pytest -s -v -m "smoke and win10" test_fixture2.py


Скипать тест - привязать маркер @pytest.mark.skip
           
падающий тест -  @pytest.mark.xfail(reason="fixing this bug right now") (когда он неожиданно пройдет будет помечаться XPASS в консоли 

"""
