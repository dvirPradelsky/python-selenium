from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class ElementsPageData:
    URL_PAGE = '/elements'

    TEXT_BOX_HEADER = 'Text Box'
    TEXT_BOX_FULL_NAME_LABEL = 'Full Name'
    TEXT_BOX_FULL_NAME_PLACEHOLDER = 'Full Name'
    TEXT_BOX_EMAIL_LABEL = 'Email'
    TEXT_BOX_EMAIL_PLACEHOLDER = 'name@example.com'
    TEXT_BOX_CURRENT_ADDRESS_LABEL = 'Current Address'
    TEXT_BOX_CURRENT_ADDRESS_PLACEHOLDER = 'Current Address'
    TEXT_BOX_PERMANENT_ADDRESS_LABEL = 'Permanent Address'
    TEXT_BOX_SUBMIT_BUTTON_TEXT = 'Submit'
    TEXT_BOX_CONFIRM_DATA_NAME = 'Name: '
    TEXT_BOX_CONFIRM_DATA_EMAIL = 'Email: '
    TEXT_BOX_CONFIRM_DATA_CURRENT_ADDRESS = 'Current Address: '
    TEXT_BOX_CONFIRM_DATA_PERMANENT_ADDRESS = 'Permanent Address: '


class ElementsPage(BasePage):

    def __init__(self, driver, navigate_to_elements=True):
        super().__init__(driver)
        self.data = ElementsPageData()
        if navigate_to_elements:
            self.go_to_url(self.data.URL_PAGE)
        self.logo = (By.XPATH, '//*[@id="app"]/header/a/img/abc')
        self.items_list = (By.XPATH, '//*[@id="app"]//div/h5')
        self.elements_text_box_item = (By.XPATH, '(//*[@ id="item-0"])[1]')
        self.elements_text_box_item_header = (By.XPATH, '//h1[text() = "Text Box"]')
        self.elements_text_box_full_name_label_sel = (By.ID, 'userName-label')
        self.elements_text_box_full_name_input_sel = (By.ID, 'userName')
        self.elements_text_box_email_label_sel = (By.ID, 'userEmail-label')
        self.elements_text_box_email_input_sel = (By.ID, 'userEmail')
        self.elements_text_box_current_address_label_sel = (By.ID, 'currentAddress-label')
        self.elements_text_box_current_address_input_sel = (By.ID, 'currentAddress')
        self.elements_text_box_permanent_address_label_sel = (By.ID, 'permanentAddress-label')
        self.elements_text_box_permanent_address_input_sel = (By.ID, 'permanentAddress')
        self.elements_text_box_submit_button_sel = (By.ID, 'submit')

        self.elements_text_box_name_result_sel = (By.ID, 'name')
        self.elements_text_box_email_result_sel = (By.ID, 'email')
        self.elements_text_box_current_address_result_sel = (By.XPATH, '//p[@id="currentAddress"]')
        self.elements_text_box_permanent_address_result_sel = (By.XPATH, '//p[@id="permanentAddress"]')

    @property
    def elements_text_box_list_item(self):
        text_box_item = self.driver.find_element(*self.elements_text_box_item)
        return text_box_item

    @property
    def elements_text_box_header(self):
        text_box_header = self.driver.find_element(*self.elements_text_box_item_header)
        return text_box_header

    @property
    def elements_text_box_full_name_label(self):
        full_name_label = self.driver.find_element(*self.elements_text_box_full_name_label_sel)
        return full_name_label

    @property
    def elements_text_box_full_name_input(self):
        full_name_input = self.driver.find_element(*self.elements_text_box_full_name_input_sel)
        return full_name_input

    @property
    def elements_text_box_email_label(self):
        email_label = self.driver.find_element(*self.elements_text_box_email_label_sel)
        return email_label

    @property
    def elements_text_box_email_input(self):
        email_input = self.driver.find_element(*self.elements_text_box_email_input_sel)
        return email_input

    @property
    def elements_text_box_current_address_label(self):
        current_address_label = self.driver.find_element(*self.elements_text_box_current_address_label_sel)
        return current_address_label

    @property
    def elements_text_box_current_address_input(self):
        current_address_input = self.driver.find_element(*self.elements_text_box_current_address_input_sel)
        return current_address_input

    @property
    def elements_text_box_permanent_address_label(self):
        permanent_address_label = self.driver.find_element(*self.elements_text_box_permanent_address_label_sel)
        return permanent_address_label

    @property
    def elements_text_box_permanent_address_input(self):
        permanent_address_input = self.driver.find_element(*self.elements_text_box_permanent_address_input_sel)
        return permanent_address_input

    @property
    def elements_text_box_submit_button(self):
        submit_button = self.driver.find_element(*self.elements_text_box_submit_button_sel)
        return submit_button






    @property
    def elements_text_box_name_result(self):
        name_result = self.driver.find_element(*self.elements_text_box_name_result_sel)
        return name_result

    @property
    def elements_text_box_email_result(self):
        email_result = self.driver.find_element(*self.elements_text_box_email_result_sel)
        return email_result

    @property
    def elements_text_box_current_address_result(self):
        current_address_result = self.driver.find_element(*self.elements_text_box_current_address_result_sel)
        return current_address_result

    @property
    def elements_text_box_permanent_address_result(self):
        permanent_address_result = self.driver.find_element(*self.elements_text_box_permanent_address_result_sel)
        return permanent_address_result

    def elements_text_box_fill_form(self, full_name: str = None, email: str = None, current_address: str = None,
                                    permanent_address: str = None):
        if not any([full_name, email, current_address, permanent_address]):
            raise ValueError("Required at least one parameter")
        if full_name is not None:
            self.elements_text_box_full_name_input.send_keys(full_name)
        if email is not None:
            self.elements_text_box_email_input.send_keys(email)
        if current_address is not None:
            self.elements_text_box_current_address_input.send_keys(current_address)
        if permanent_address is not None:
            self.elements_text_box_permanent_address_input.send_keys(permanent_address)
