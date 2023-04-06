import time
from login_page import Login_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем класс нашего домашнего задания
class Test_3_dz():

    # открываем сайт с использованием webdriver
    def all_login(self):
        service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)
        print("Open page")

        # создаем список пользователей
        login_list = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]

        # создаём пароль один общий для всех пользователей
        standart_password = "secret_sauce"

        # авторизуемся под каждым пользователем и проверяем в зависимости от логина нужное поведение
        for f in login_list:
            if f == "locked_out_user":
                login = Login_page(driver=driver)
                login.authorization(login_name=f, login_password=standart_password)
                print("Authorization is bad!")
                # считываем сообщение об ошибке для этого пользователя
                error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
                error_message_actual = error_message.text
                # проверяем сообщение об ошибки при попытке авторизоваться locked пользователем
                error_message_expected = "Epic sadface: Sorry, this user has been locked out."
                assert error_message_expected == error_message_actual
                print("User locked_out_user is Successfully!")
                driver.refresh()
            elif f == "performance_glitch_user":
                login = Login_page(driver=driver)
                login.authorization(login_name=f, login_password=standart_password)
                print("Authorization is passed")
                # проверяем что мы зашли на главную страницу
                main_page = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
                main_page_actual = main_page.text
                main_page_expected = "PRODUCTS"
                assert main_page_expected == main_page_actual
                print("User performance_glitch_user is Successfully!")
                # разлогиниваемся, для этого сначала ищем кнопку menu
                menu_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
                menu_button.click()
                print("Click menu button")
                # теперь ищем кнопку logout
                logout_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
                logout_button.click()
                print("Click logout button")
            else:
                login = Login_page(driver=driver)
                login.authorization(login_name=f, login_password=standart_password)
                print("Authorization is Successfully!")
                # проверяем что зашли на главную страницу
                main_page = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
                main_page_actual = main_page.text
                main_page_expected = "PRODUCTS"
                assert main_page_expected == main_page_actual
                print(f'User {f}  is Successfully!')
                # ищем кнопку menu
                menu_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
                menu_button.click()
                print("Click menu button")
                # теперь ищем кнопку logout и выходим из приложения
                logout_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
                logout_button.click()
                print("Click logout button")

test = Test_3_dz()
test.all_login()










