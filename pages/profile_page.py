from pages.base_page import BasePage


class ProfilePage(BasePage):
    PATH = '/user'

    EMAIL_INPUT = 'input[name="reserveEmail"]'
    NAME_INPUT = 'input[name="fullname"]'
    SAVE_BTN = 'input[type="submit"]'
    LOGOUT_BTN = '#logoutButton'
    CHANGE_PASSWORD_BTN = '#changePasswordButton'
    BACK_BTN = '.back-btn'
    EMAIL_ERROR = '#reserveEmailErrorText'

    def __init__(self, driver):
        super().__init__(driver, 'div.profile')

    def set_email(self, email):
        el = self.locate_el(self.EMAIL_INPUT)
        el.clear()
        el.send_keys(email)

    def set_name(self, name):
        el = self.locate_el(self.NAME_INPUT)
        el.clear()
        el.send_keys(name)

    def click_save_btn(self):
        self.locate_el(self.SAVE_BTN).click()

    def click_logout_btn(self):
        self.locate_el(self.LOGOUT_BTN).click()

    def click_change_password_btn(self):
        self.locate_el(self.CHANGE_PASSWORD_BTN).click()

    def click_back_btn(self):
        self.locate_el(self.BACK_BTN).click()

    def get_email(self):
        return self.locate_el(self.EMAIL_INPUT).get_attribute('value')

    def get_name(self):
        return self.locate_el(self.NAME_INPUT).get_attribute('value')

    def get_email_error(self):
        return self.locate_el(self.EMAIL_ERROR).text
