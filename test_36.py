
""" 3.6 Параметризация тестов """


import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

answer = math.log(int(time.time()))

# link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(driver, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver.get(link)
    driver.find_element_by_css_selector("#login_link")




""" эта фикстура находится в файле conftest
@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = WebDriver(executable_path='C:\Python33\chromedriver_win32\chromedriver')
    # этот код выполнится после завершения теста
    yield driver
    print("\nquit browser..")
    driver.quit()
"""

# В этом задании нужно передать ссылки в качестве параметров
@pytest.mark.parametrize ('paramlinkk', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
class TestParam1 ():

    @pytest.fixture
    def driver(self):
        print("\nstart browser for test..")
        driver = WebDriver(executable_path='C:\Python33\chromedriver_win32\chromedriver')
        yield driver
        # этот код выполнится после завершения теста
        print("\nquit browser..")
        driver.quit()



    def test_param (self, driver, paramlinkk):
        link = f'https://stepik.org/lesson/{paramlinkk}/step/1'
        driver.get(link)
        #явное ожидание
        element1 = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
        )
        answer = (math.log(int(time.time())))
        input1 = driver.find_element_by_css_selector(".textarea").send_keys(str(answer))
        button1 = driver.find_element_by_css_selector(".submit-submission").click()

        cheked1 = WebDriverWait (driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        assert "Correct!" in cheked1.text
        time.sleep(3)



