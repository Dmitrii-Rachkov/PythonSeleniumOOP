import time

from login_page import Login_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_2():

    def test_select_product(self):
        service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)
        print("Start test")

        standart_user = "standard_user"
        standart_password = "secret_sauce"

        # Создаём переменную которая будет являться экземпляром класса login_page
        login = Login_page(driver=driver)
        # Используем метод из класса для авторизации, при этом передавая переменные логина и пароля
        login.authorization(login_name=standart_user, login_password=standart_password)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click add to cart")

        move_to_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        move_to_cart.click()
        print("Move to cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == "YOUR CART"
        print("Test successful")


test = Test_2()
test.test_select_product()

