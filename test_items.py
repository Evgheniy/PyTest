import time
from selenium.webdriver.common.by import By


def test_basket_button(browser, language):
    try:
        link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button[value]")
    except Exception as ex:
        print(ex)
    assert browser.find_element(By.CSS_SELECTOR, "button[value]"), "button not found"
