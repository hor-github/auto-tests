

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time

import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



#driver = WebDriver(executable_path='C://selenium//chromedriver.exe')
driver = WebDriver(r'/ChromeDriver/chromedriver')

def test_22 ():
    try:
        driver.get("https://fix-online.sbis.ru/business/?region_left=%D0%91%D0%B8%D0%B7%D0%BD%D0%B5%D1%81")
        #Авторизация
        input1 = driver.find_element_by_name("login").send_keys("Балаган")
        input12 = driver.find_element_by_name("password").send_keys("Балаган123")
        button = driver.find_element_by_css_selector(".auth-Form__submit").click()

        # В течение 15сек ждем текст=$100 из элемента с id=price
        # price2 = WebDriverWait(driver, 15).until(
        #    EC.element_located_to_be_selected(By.CSS_SELECTOR,
        #                                      ".controls-Grid__row-cell_selected > div:nth-child(1) > span")
        # )
        time.sleep(5)
        buttonsale = driver.find_element_by_css_selector(".controls-Grid__row-cell_selected > div:nth-child(1) > span:nth-child(1)").click()


        # Заходим в каталог
        time.sleep(10)
        link1 = driver.find_element_by_css_selector("a.NavigationPanels-Accordion__item:nth-child(5)").click()

        alert = driver.switch_to_alert()
        alert.dismiss()

        # Ожидание кнопки "Отчеты"
        buttonreports = WebDriverWait(driver, 15).until(
                EC.element_located_to_be_selected((By.CSS_SELECTOR, ".controls-text-link_theme-default"))
             )

        buttonreports.click()


        time.sleep(5)
        button2 = driver.find_element_by_css_selector("div.controls-DropdownList__row:nth-child(12)").click()
        time.sleep(2)
        button3 = driver.find_element_by_css_selector("div.controls-Scroll:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()

        price = driver.find_element_by_link_text('Прайс').click()

    finally:
        time.sleep(10)
        driver.quit()
