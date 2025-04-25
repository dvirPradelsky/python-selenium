from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class HomePageData:
    URL = "https://demoqa.com/"

    ELEMENTS = "Elements"
    FORMS = 'Forms'
    ALERTS_FRAME_WINDOWS = "Alerts, Frame & Windows"
    WIDGETS = "Widgets"
    INTERACTIONS = "Interactions"
    BOOK_STORE_APPLICATIONS = "Book Store Application"


class HomePage(BasePage):
    def __init__(self, driver, navigate_to_home=True):
        super().__init__(driver)
        if navigate_to_home:
            self.go_to_url()
        self.data = HomePageData()
        self.home_screen_logo = (By.XPATH, '//*[@id="app"]/header/a/img')
        self.items_list = (By.XPATH, '//*[@id="app"]//div/h5')

    @property
    def logo_element(self):
        logo_image = self.driver.find_element(*self.home_screen_logo)
        return logo_image

    def get_item(self, index):
        items_list = self.driver.find_elements(*self.items_list)
        return items_list[index]
