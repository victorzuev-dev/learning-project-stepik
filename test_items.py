from selenium.webdriver.common.by import By
import time

link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_basket_button_on_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.ID, "add_to_basket_form")
    basket_button.click()
    time.sleep(2)
    basket = browser.find_element(By.CLASS_NAME, "basket-mini")
    summ_in_basket = basket.text.split(" ")[3]
    assert summ_in_basket != "0,00"
