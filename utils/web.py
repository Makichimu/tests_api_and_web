from selenium.webdriver.common.by import By
from utils.response_saver import save_response_to_file_web as sw


class WEB:

    base_url = "https://reqres.in/"

    def find_and_click(self, driver, css_selector):
        driver.get(self.base_url)
        sample_request_button = driver.find_element(By.CSS_SELECTOR, css_selector)
        sample_request_button.click()

    def get_response_body_and_status(self, driver):
        status_code_element = driver.find_element(By.CSS_SELECTOR,
                                                  "#console > div.output > div.response > p > strong > span")
        status_code_text = status_code_element.text
        status_code = int(status_code_text)
        if status_code == 204:
            response_body_text = "{}"
        else:
            response_body_element = driver.find_element(By.CSS_SELECTOR, "#console > div.output > div.response > pre")
            response_body_text = response_body_element.text
        sw(response_body_text, status_code_text, 'web_response.json')


