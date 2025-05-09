from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

ONE_MILLISECOND = 1000

class SeleniumClient:
    
    @staticmethod
    def report_locust_event(events, name, start_time, exception=None):
        total_time = int((time.time() - start_time) * ONE_MILLISECOND)  # em ms
        events.request.fire(
            request_type="SELENIUM",
            name=name,
            response_time=total_time,
            response_length=0,
            exception=exception
        )        
    
    def __init__(self, headless=True, window_size="1920,1080"):
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument(f'--window-size={window_size}')
        self.driver = webdriver.Chrome(options=options)

    def get(self, url):
        self.driver.get(url)

    def wait_and_click_xpath(self, by, locator, wait):
        element = WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def quit(self):
        self.driver.quit()

