from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_on_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.ID, "add_to_basket_form")
    assert basket_button.is_displayed()  # проверка отображения кнопки на странице

