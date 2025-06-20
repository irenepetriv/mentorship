from pages.base_page import BasePage
from playwright.sync_api import Page


class SecondPage(BasePage):
    forms_button = '//*[@class="header-text" and text()="Forms"]'
    practice_form_button = '//*[@class="element-list collapse show"]'

    def click_forms_button(self):
        self.get_element(self.forms_button).click()

    def click_practice_forms_button(self):
        self.get_element(self.practice_form_button).click()
