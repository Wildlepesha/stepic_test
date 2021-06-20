import time


class TestStepic():
    def test_one(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(5)
        browser.set_window_size("1720", "900")

        button = browser.find_element_by_class_name("btn-add-to-basket").click()
        text = browser.find_element_by_css_selector("#messages > div:nth-child(1) > div > strong").text

        assert text == "Coders at Work", f"Wrong book was added, expected Coders at Work, but got {text}"
