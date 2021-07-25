# pytest --language=es test_items.py 
import time
from selenium.webdriver.common.by import By


def test_find_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    time.sleep(1)
    button = browser.find_element(By.XPATH, '//button[text()="Añadir al carrito"]').text
    assert 'Añadir al carrito' == button, "Error, different localization!"
