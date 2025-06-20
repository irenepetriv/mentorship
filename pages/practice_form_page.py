from pages.base_page import BasePage
from playwright.sync_api import Page


class PracticeFormPage(BasePage):
    first_name_input = '//*[@id="firstName"]'
    last_name_input = '//*[@id="lastName"]'
    email_input = '//*[@id="userEmail"]'
    gender_input = '//*[@class="custom-control-label" and text()="Female"]'
    mobile_phone_input = '//*[@id="userNumber"]'
    date_of_birth_input = '//*[@id="dateOfBirthInput"]'
    select_birth_date = '//div[@class="react-datepicker"]//*[@role="listbox"]//*[@role="option" and text()="18"]'
    subject_input = '//*[@id="subjectsInput"]'
    hobbies_input = '//*[@class="custom-control-label" and text()="Music"]'
    address_input = '//*[@id="currentAddress"]'
    state_input = '//*[@id="state"]'
    state_option = '//*[@id="react-select-3-option-0"]'
    city_input = '//*[@id="city"]'
    city_option = '//*[@id="react-select-4-option-0"]'
    submit_button = '//*[@id="submit"]'

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def first_name(self):
        return self.get_element(self.first_name_input).input_value()

    @first_name.setter
    def first_name(self, name: str):
        self.fill_input(self.first_name_input, name)

    @property
    def last_name(self):
        return self.get_element(self.last_name_input).input_value()

    @last_name.setter
    def last_name(self, name: str):
        self.fill_input(self.last_name_input, name)

    @property
    def email(self):
        return self.get_element(self.email_input).input_value()

    @email.setter
    def email(self, name: str):
        self.fill_input(self.email_input, name)

    def select_gender_female(self):
        self.get_element(self.gender_input).click()

    @property
    def mobile_phone(self):
        return self.get_element(self.mobile_phone_input).input_value()

    @mobile_phone.setter
    def mobile_phone(self, name: str):
        self.fill_input(self.mobile_phone_input, name)

    def click_date_of_birth(self):
        self.get_element(self.date_of_birth_input).click()

    def select_birthday(self):
        self.get_element(self.select_birth_date).click()

    @property
    def subject(self):
        return self.get_element(self.subject_input).input_value()

    @subject.setter
    def subject(self, name: str):
        self.fill_input(self.subject_input, name)

    def select_hobbies(self):
        self.get_element(self.hobbies_input).click()

    @property
    def address(self):
        return self.get_element(self.address_input).input_value()

    @address.setter
    def address(self, name: str):
        self.fill_input(self.address_input, name)

    def click_state(self):
        self.get_element(self.state_input).click()

    def select_state(self, state_name: str = "NCR"):
        self.get_element(self.state_option.format(state_name)).click()

    def click_city(self):
        self.get_element(self.city_input).click()

    def select_city(self, city_name: str = "Delhi"):
        self.get_element(self.city_option.format(city_name)).click()

    def click_submit(self):
        self.get_element(self.submit_button).click()
