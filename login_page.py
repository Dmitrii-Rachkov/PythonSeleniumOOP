from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Принципы Page Object Model"""

# POM - это значит что у каждой страницы приложения будет отдельный класс, отдельный метод,
# который будет содержать в себе все локаторы, все шаги и действия, которые совершаются
# на конкретной данной странице.

# Login_page - стандартное название страницы авторизации

# Создаём модуль авторизации
# При создании экземпляра класса Login_page нам необходимо передать наш driver
# При использовании метода authoriztion нам необходимо передать два аргумента - логин и пароль

class Login_page():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        user = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user.send_keys(login_name)
        print("Input login")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(login_password)
        print("Input password")

        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        login_button.click()
        print("Click login button")