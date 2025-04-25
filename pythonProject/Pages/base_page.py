from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    base_url = "https://demoqa.com/"
    
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, path=None):
        if path is None:
            self.driver.get(self.base_url)
        else:
            full_url = f'{self.base_url.rstrip("/")}/{path.lstrip("/")}'
            self.driver.get(full_url)

    def verify_current_url(self, expected_url, include_base_url=True):
        actual_url = self.driver.current_url
        if include_base_url:
            expected_url = f'{self.base_url.rstrip("/")}/{expected_url.lstrip("/")}'
        assert_that(actual_url, 'Verify current url').is_equal_to(expected_url)

    def scroll_down(self, max_scroll_attempts=2, scroll_pause_time=2):
        """
        Scroll down on web page
        """
        scroll_height = 500

        for _ in range(max_scroll_attempts):
            self.driver.execute_script(f"window.scrollTo(0, {scroll_height});")
            time.sleep(scroll_pause_time)
            scroll_height += 500
