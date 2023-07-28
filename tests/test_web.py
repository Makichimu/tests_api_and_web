import pytest
from tests.selectors_names_of_api_tests import tests
from utils.web import WEB

import time
import json

class TestWeb(WEB):

    def test_homepage(self, driver):
        driver.get(self.base_url)
        assert "Reqres" in driver.title

    @pytest.mark.parametrize("css_selector,test_name", tests)
    def test_send_sample_requests(self, driver, css_selector, test_name):
        print(f"Сохраняем результаты для {test_name}")
        self.find_and_click(driver, css_selector)
        if test_name == "test_get_delayed_response":
            time.sleep(4)
        self.get_response_body_and_status(driver)

    def test_compare_api_and_web_responses(self):
        with open('api_response.json', 'r') as f:
            api_responses = json.load(f)
        with open('web_response.json', 'r') as f:
            web_responses = json.load(f)

        def remove_fields(d):
            for field in ['id', 'createdAt', 'updatedAt']:
                d.pop(field, None)
            return d

        api_responses = [remove_fields(response) for response in api_responses]
        web_responses = [remove_fields(response) for response in web_responses]

        assert api_responses == web_responses, "Апи и Веб не совпадают!"







