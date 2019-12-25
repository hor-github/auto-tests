from selenium.webdriver.chrome.webdriver import WebDriver
import time


driver = WebDriver(executable_path='C://selenium//chromedriver.exe') #указать свой путь до драйвера



def test_search_elements_step_10 ():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        driver.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = driver.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("George")
        input2 = driver.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Visshii")
        input3 = driver.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("Visshii")
        input4 = driver.find_element_by_xpath("//input[@placeholder='Input your phone:']")
        input4.send_keys("Visshii")
        input5 = driver.find_element_by_xpath("//input[@placeholder='Input your address:']")
        input5.send_keys("Visshii")


        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        driver.quit()