import time


class TestStepic():
    def test_one(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(5)
        browser.set_window_size("1720", "900")

        button = browser.find_element_by_class_name("btn-add-to-basket").click()

        # На этом начинается мои фантазии, потому что поиск кнопки слишком скучно и ассерт не будет срабатывать,
        # если элемент не будет найден, поэтому я решил проверить на сообщение об успешном добавлении товара в корзину

        alert_success = browser.find_element_by_css_selector("#messages > div:nth-child(1)")
        alert_success_class = alert_success.get_attribute("class")

        # time.sleep(30)

        assert "alert-success" in alert_success_class, "Expected to find alert-success bootstrap attribute"
