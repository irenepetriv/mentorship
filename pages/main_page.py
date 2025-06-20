from pages.base_page import BasePage
from playwright.sync_api import Page


class MainFirstPage(BasePage):
    forms_card_input = '//*[@class="category-cards"]//*[@class="card mt-4 top-card"][2]'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def click_forms_card(self):
        self.get_element(self.forms_card_input).click()


