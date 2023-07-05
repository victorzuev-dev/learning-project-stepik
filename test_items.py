from selenium.webdriver.common.by import By

import time

link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_basket_button_on_page(browser):
    browser.get(link)
    time.sleep(5)
    # проверка наличия кнопки добавления в корзину
    browser.find_element(By.ID, "add_to_basket_form")