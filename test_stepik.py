from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time
import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = WebDriver(executable_path='C://selenium//chromedriver.exe')

#Говорим WebDriver ждать 5 сек
#driver.implicitly_wait(15)

def test_lesson6_step3():

# try\finally закрыввает браузер после свех операций даже если тест упал
    try:
        link = "http://suninjuly.github.io/simple_form_find_task.html"
        driver.get(link)
        input1 = driver.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = driver.find_element_by_id("country")
        input4.send_keys("Russia")
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        driver.quit()

# не забываем оставить пустую строку в конце файла




def test_search_elements_4 ():
    # ищем нужную ссылку и кликаем на нее
    driver.get("http://suninjuly.github.io/find_link_text")
    a = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = driver.find_element_by_link_text(a)
    link.click()

    # заполняем форму
    try:
        input1 = driver.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = driver.find_element_by_id("country")
        input4.send_keys("Russia")
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        driver.quit()


def test_search_elements_7():

    try:
        driver.get("http://suninjuly.github.io/huge_form.html")
        elements = driver.find_elements_by_css_selector(".first_block input")
        for element in elements:
            element.send_keys("Мой")

        button = driver.find_element_by_xpath("//button")
      #  button = driver.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        driver.quit()

    # не забываем оставить пустую строку в конце файла



def test_search_elements_8 ():
    # ищем нужную ссылку и кликаем на нее
    driver.get("http://suninjuly.github.io/find_xpath_form ")
    # заполняем форму
    try:
        input1 = driver.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = driver.find_element_by_id("country")
        input4.send_keys("Russia")
        button = driver.find_element_by_xpath("//button[@type='submit']")   #//button[[@type= 'submit']
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        driver.quit()



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




def test2_1_step5 ():
    try:
        driver.get("http://suninjuly.github.io/math.html")

        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        x_element = driver.find_element_by_id ("input_value")

        x = x_element.text
        y = calc(x)
        input1 = driver.find_element_by_xpath("//input[@id='answer']").send_keys(y)
        input2 = driver.find_element_by_xpath("//input[@id='robotCheckbox']").click()
        input3 = driver.find_element_by_xpath("//input[@id ='robotsRule']").click()
        button = driver.find_element_by_xpath("//*[@class='btn btn-default']").click()

        # Находит по селектору и на все кликает
        # for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
        #     browser.find_element_by_css_selector(selector).click()

    finally:
        time.sleep(10)

        driver.quit()


def test_21_step7 ():
    try:
        driver.get("http://suninjuly.github.io/get_attribute.html")


        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        x_element = driver.find_element_by_css_selector("#treasure")
        x = x_element.get_attribute("valuex")
        y = calc(x)

        input1 = driver.find_element_by_xpath("//*[@id='answer']").send_keys(y)

        input2 = driver.find_element_by_xpath("//input[@id='robotCheckbox']").click()

        input3 = driver.find_element_by_xpath("//input[@id ='robotsRule']").click()

        button = driver.find_element_by_xpath("//*[@class='btn btn-default']").click()

    finally:
        time.sleep(10)

        driver.quit()

#Работа с выпадающими списками
def test_22_step3 ():
    try:
        driver.get("http://suninjuly.github.io/selects1.html")

        def calc(x,y):
            return str(int(x) + int(y))

        num1 = driver.find_element_by_id("num1")
        x = num1.text
        num2 = driver.find_element_by_xpath("//*[@id='num2']")
        y = num2.text
        z = calc(x,y)

        #Выпадающий список
        select = Select(driver.find_element_by_tag_name("select"))
        select.select_by_value(z)
        button = driver.find_element_by_xpath("//button").click()

    finally:
        time.sleep(10)
        driver.quit()



 #Прокрутка страницы до нужного элемента
def test_22_step6 ():
    try:
        link = "http://SunInJuly.github.io/execute_script.html"
        driver.get(link)
        x = driver.find_element_by_id("input_value").text

        #РАссчитываем X и присваем результат переменной Z
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        z = calc(x)

        button = driver.find_element_by_tag_name("button")

        # прокручиваем страницу до кнопки
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        input1 = driver.find_element_by_xpath("//input[@class = 'form-control']").send_keys(z)
        inputCheckBox = driver.find_element_by_xpath("//input[@id ='robotCheckbox']").click()

        # прокручиваем страницу до radiobutton и кликаем
        inputRadiobutton = driver.find_element_by_xpath("//input[@id ='robotsRule']")
        driver.execute_script("return arguments[0].scrollIntoView(true);", inputRadiobutton)
        inputRadiobutton.click()

        # прокручиваем страницу до кнопки
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
    finally:
        time.sleep(10)
        driver.quit()


# Прикрепление файла
def test_22_step_8 ():
    try:
        driver.get("http://suninjuly.github.io/file_input.html")

        input1 = driver.find_element_by_xpath("//input[@name='firstname']").send_keys("GO")
        input2 = driver.find_element_by_xpath("//input[@name='lastname']").send_keys("R")
        input3 = driver.find_element_by_xpath("//input[@name='email']").send_keys("@")

        input4 = driver.find_element_by_xpath("//input[@name='file']")

# прописываем путь до нужного файла
        current_dir = os.path.abspath(os.path.dirname("C:/Program Files (x86)/Python/file.txt"))
        file_path = os.path.join(current_dir, 'file.txt')
        input4.send_keys(file_path)

        button = driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()
    finally:
        time.sleep(10)
        driver.quit()


# Работа с окнами alert
def test_23_step_3 ():
    try:
        driver.get("http://suninjuly.github.io/alert_accept.html")

        button = driver.find_element_by_css_selector("button.btn").click()

        # принимаем confirm
        confirm1 = driver.switch_to.alert.accept()

        x = driver.find_element_by_css_selector("span#input_value").text

        # Рассчитываем calcX и присваем результат переменной Z
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        z = calc(x)

        #Помещаем в инпут результат функции
        input1 = driver.find_element_by_css_selector("input#answer").send_keys(z)

        button2 = driver.find_element_by_css_selector("button.btn").click()

    finally:
        time.sleep(10)
        driver.quit()


# Работа со вкладками
def test_23_step_5 ():
    try:
        driver.get("http://suninjuly.github.io/redirect_accept.html")
        button = driver.find_element_by_css_selector("button.trollface")
        time.sleep(3)
        button.click()

        # Переходим на другую вкладку
        window2 = driver.window_handles[1]  # 1  - номер вкладки
        driver.switch_to.window(window2)    # переключаемся на вторую вкладку

        # Получаем текст из переменной X
        x = driver.find_element_by_css_selector("span#input_value").text

        # Рассчитываем calcX и присваем результат переменной Z
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        z = calc(x)

        # Помещаем в инпут результат функции
        input1 = driver.find_element_by_css_selector("input#answer").send_keys(z)

        button2 = driver.find_element_by_css_selector("button.btn").click()
    finally:
        time.sleep(10)
        driver.quit()



def test24_step_8 ():
    try:
        driver.get("http://suninjuly.github.io/explicit_wait2.html")

# В течение 15сек ждем текст=$100 из элемента с id=price
        price2 = WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
            )
        button = driver.find_element_by_css_selector('button#book').click()

# Получаем текст из переменной X
        x = driver.find_element_by_css_selector("span#input_value").text

# Рассчитываем calcX и присваем результат переменной Z
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        print(x)
        z = calc(x)

# Помещаем в инпут результат функции
        input1 = driver.find_element_by_css_selector("input#answer").send_keys(z)
        button2 = driver.find_element_by_css_selector("button#solve").click()

    finally:
        time.sleep(10)
        driver.quit()





    print("commit for bugFix 28.12")

    print("commit for master 28.12")